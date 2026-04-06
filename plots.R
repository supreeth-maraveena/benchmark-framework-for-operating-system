library(ggplot2)

# Load data
data <- read.csv("results.csv", stringsAsFactors = FALSE)

# Sort (higher is better)
data <- data[order(-data$Score), ]

# Top 5
top <- head(data, 5)

# Add rank
top$Rank <- paste0("#", 1:nrow(top))

# Highlight best policy
top$Color <- ifelse(top$Score == max(top$Score), "Best", "Others")

# Plot
ggplot(top, aes(x = reorder(Combination, Score), y = Score, fill = Color)) +
  
  # Bars
  geom_col(width = 0.6) +
  
  # Value labels
  geom_text(aes(label = round(Score, 3)),
            hjust = -0.15,
            size = 5,
            fontface = "bold") +
  
  # Rank labels on left
  geom_text(aes(label = Rank),
            hjust = 1.2,
            color = "black",
            size = 4,
            fontface = "bold") +
  
  # Horizontal
  coord_flip() +
  
  # Colors
  scale_fill_manual(values = c("Best" = "#27AE60", "Others" = "#2E86AB")) +
  
  # Titles
  labs(
    title = "Top 5 Policy Combinations",
    subtitle = "Normalized Performance (Best = 1)",
    x = "",
    y = "Normalized Score",
    fill = ""
  ) +
  
  # Expand space for labels
  expand_limits(y = max(top$Score) * 1.15) +
  
  # Theme
  theme_minimal(base_size = 14) +
  theme(
    plot.title = element_text(face = "bold", size = 20, hjust = 0.5),
    plot.subtitle = element_text(size = 12, color = "gray40", hjust = 0.5),
    
    axis.text.y = element_text(size = 11, face = "bold"),
    axis.text.x = element_text(size = 11),
    
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    
    legend.position = "none"
  )