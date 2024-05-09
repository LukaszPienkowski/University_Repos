library(ggplot2)
library(dplyr)
library(tidyr)
library(lubridate)
library(tm)
library(wordcloud)
library(sentimentr)
library(stringr)

setwd('C:\\Users\\User\\Documents\\UW - magisterskie\\Advanced Visualisation in R\\Projekt')

df_bf <- read.csv('CompleteTrumpTweetsArchive\\data\\realDonaldTrump_bf_office.csv', sep = ',')
df_in <- read.csv('CompleteTrumpTweetsArchive\\data\\realDonaldTrump_in_office.csv', sep = ',')

df_all <- rbind(df_bf, df_in)

df_all$date <- as.Date(df_all$Time)
df_all$year <- year(as.Date(df_all$Time, format = "%Y"))


#1 Number of tweets per year
ggplot(df_all, aes(x = year)) + 
  geom_histogram(binwidth = 1, color = "black", fill = "blue") + 
  ggtitle("Number of tweets per yaer") + 
  xlab("Year") + 
  ylab("Number of tweets") + 
  theme_classic() +
  geom_vline(xintercept = 2017, color = "red", linetype = "dashed") +
  annotate("text", x=2017, y=6000, label="Year of election as president", angle=90, size=5, color="black")

#2 Word map
stop_words <- c("and", "the", "to", "of", "is", "in", "for", "realDonaldTrump", "a", "you", "realdonaldtrump", "i", "on", "will", "are",
                "be", "that", "it")
df_all$text <- sapply(df_all$Tweet.Text, function(x) {
  x <- gsub("#\\w+", "", x) 
  x <- gsub("[^[:alnum:][:space:]]", "", x) 
  x <- tolower(x)
  x <- gsub("[[:space:]]+", " ", x)
  x <- gsub("^[[:space:]]|[[:space:]]$", "", x) 
  words <- strsplit(x, " ")[[1]]
  words <- words[!words %in% stop_words]
  return(words)
})

frequent_words <- unlist(df_all$text)
frequent_words <- table(frequent_words)
frequent_words <- sort(frequent_words, decreasing = TRUE)
df1 <- data.frame(rbind(frequent_words))
df1 <- t(df1)
df1 <- cbind(word = rownames(df1), df1)
rownames(df1) <- 1:nrow(df1)
df1 <- data.frame(df1)
df1$frequent_words <- as.integer(df1$frequent_words)

wordcloud(words = df1$word, freq = df1$frequent_words, min.freq = 1,
          max.words = 100, random.order = FALSE, rot.per = 0.35, 
          colors = brewer.pal(8, "Dark2"))


#3 Sentiment analysis
df_all$sentiment <- sapply(df_all$Tweet.Text, sentiment)
ggplot(data = df_all, aes(x = "", y = 1, fill = sentiment)) +
  geom_bar(width = 1, stat = "identity") +
  coord_polar("y", start = 0) +
  ggtitle("Sentiment analysis of tweets")

#4 Most used hashtags
data_hashtags_count <- df_all %>%
  group_by(Tweet.Text) %>%
  summarize(count = n()) %>%
  arrange(desc(count))

ggplot(data_hashtags_count, aes(x = reorder(Tweet.Text, -count), y = count)) +
  geom_bar(stat = "identity") +
  xlab("#") +
  ylab("Count") +
  ggtitle("Most used hashtags") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

#5 How many emoticons
df_all$smile <- str_count(df_all$Tweet.Text, ":\\)")
df_all$sad <- str_count(df_all$Tweet.Text, ':\\(')
df_all$wink <- str_count(df_all$Tweet.Text, ';\\)')
df_all$tongue <- str_count(df_all$Tweet.Text, ':P')

df_all$emoticon <- ifelse(df_all$smile > 0, "Smile",
                          ifelse(df_all$sad > 0, "Sad",
                                 ifelse(df_all$wink > 0, "Wink",
                                        ifelse(df_all$tongue > 0, "Tongue", "None"))))

data_emoticon <- df_all %>% 
  group_by(emoticon) %>%
  summarize(count = n())

ggplot(data = data_emoticon, aes(x = emoticon, y = count)) +
  geom_bar(stat = "identity") +
  ggtitle("Frequency analysis of emoticons in tweets") +
  xlab("Emoticons") +
  ylab("Num of occurances") +
  theme(legend.position = "top")

#6 Retweets
df_all$is_rt <- str_detect(df_all$Tweet.Text, "RT")
ggplot(df_all, aes(x = is_rt)) +
  geom_bar(aes(y = (..count..)/sum(..count..))) +
  scale_y_continuous(labels = scales::percent) +
  ggtitle("Proportion of Retweets")

#7 najcześciej oznaczane osoby
df_all$mentions <- str_extract_all(df_all$Tweet.Text, "(?<=@ )[^\\s]+")
tmpmen <- data.frame(matrix(NA, nrow = 35677))
tmpmen$mentions <- unlist(df_all$mentions)
mentions_count <- count(tmpmen, mentions)
mentions_count <- arrange(mentions_count, desc(n))
mentions_count <- head(mentions_count, 10)

ggplot(mentions_count, aes(x = mentions, y = n)) +
  geom_bar(stat = "identity") +
  ggtitle("15 Most Mentioned Users") +
  xlab("Mentioned Users") +
  ylab("Count") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))

#8 MAGA
df_all$magacount <- str_count(df_all$Tweet.Text, c("Make America Great Again", "Make America Great Again!", "MAGA"))
tweets_grouped <- group_by(df_all, year)
tweets_grouped <- summarize(tweets_grouped, maga_count = sum(magacount))
ggplot(tweets_grouped, aes(x = year, y = maga_count)) +
  geom_bar(stat = "identity") +
  ggtitle("'Make America Great Again' count by year") +
  xlab("Year") +
  ylab("Count")

#9 Fraud, stolen
df_all$fraudcount <- str_count(df_all$Tweet.Text, c("Fraud", "Stolen", 'fraud', 'stolen'))
tweets_grouped <- group_by(df_all, year)
tweets_grouped <- summarize(tweets_grouped, fraud_count = sum(fraudcount))
ggplot(tweets_grouped, aes(x = year, y = fraud_count)) +
  geom_bar(stat = "identity") +
  ggtitle("'Fraud/stolen' count by year") +
  xlab("Year") +
  ylab("Count")



