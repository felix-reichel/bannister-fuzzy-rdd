parse_mark <- function(mark) {
  mark <- gsub("\n", "", mark)
  mark <- trimws(mark)
  mark <- gsub("\\s.*$", "", mark)
  is_valid_format <- grepl("\\d{2}:\\d{2}\\.\\d{2}$", mark) | grepl("\\d{2}:\\d{2},\\d{1,2}$", mark) | grepl("\\d{2}:\\d{2},\\d{1}h$", mark)
  parsed_mark <- ifelse(is_valid_format, {
    mark <- gsub("h$", ":00,", mark)
    mark <- gsub(",", ".", mark)
    mark_parts <- strsplit(mark, ":")[[1]]
    minutes <- as.numeric(mark_parts[1])
    seconds_parts <- strsplit(mark_parts[2], "[.,]")[[1]]
    seconds <- as.numeric(seconds_parts[1])
    hseconds <- as.numeric(seconds_parts[2])
    total_seconds <- minutes * 60 + seconds + hseconds / 100
    total_seconds
  }, NA)
  return(as.numeric(parsed_mark))
}


### PREDICTIVE MODEL FEATURE EXTRACTION VIA RANDOM FOREST ###

library(randomForest)

data <- read.csv('world_athletics_5000m_men_results.csv')
data$mark_timedelta <- sapply(data$mark, parse_mark)
data <- data[complete.cases(data$mark_timedelta), ]
data <- data %>%
  mutate_all(~trimws(gsub("\n", "", .)))
data$date <- as.Date(data$date, format = "%d %b %Y")
data_clean <- data[, colSums(is.na(data)) < nrow(data)]
data_clean <- data_clean[complete.cases(data_clean), ]
data_clean$mark_timedelta <- as.numeric(data_clean$mark_timedelta)

set.seed(123)
train_indices <- sample(1:nrow(data_clean), 0.8 * nrow(data_clean))
train_data <- data_clean[train_indices, ]
test_data <- data_clean[-train_indices, ]

rf_model <- randomForest(mark_timedelta ~ . - mark - result_score - rank -venue, data = train_data)
predictions <- predict(rf_model, test_data)
rmse <- sqrt(mean((predictions - test_data$mark_timedelta)^2))
cat("RMSE:", rmse, "\n")
mae <- mean(abs(predictions - test_data$mark_timedelta))
cat("MAE:", mae, "\n")
mape <- mean(abs((predictions - test_data$mark_timedelta) / test_data$mark_timedelta)) * 100
cat("MAPE:", mape, "%\n")
rsquared <- 1 - (sum((test_data$mark_timedelta - predictions)^2) / sum((test_data$mark_timedelta - mean(test_data$mark_timedelta))^2))
cat("R^2:", rsquared, "\n")
# -0,03

varImpPlot(rf_model)
plot(rf_model)




### LASSO REGRESSION ###
### Possible covariates for a predictive model ###
# Covariates on Athletes
# Covariates on Stadion (Underground)
# Covariates on Historic Weather
library(glmnet)

# data$dob <- as.integer(data$dob)
# data$pos <- as.factor(data$pos)
data$date <- as.integer(data$date)


X <- model.matrix(~ date, data = data)
y <- as.numeric(data$mark_timedelta)

lasso_model <- cv.glmnet(X, y, alpha = 1)

plot(lasso_model)

best_lambda <- lasso_model$lambda.min
best_lambda

lasso_model_final <- glmnet(X, y, alpha = 1, lambda = best_lambda)

coefficients <- coef(lasso_model_final)
print(coefficients)

