# Capturing Lasting Advertising Effects with the Weibull Transformation

When it comes to advertising, the impact isn’t usually one and done—it lasts and unfolds over time. Traditional adstock models, like geometric decay, assume an immediate, steady decline in impact, which falls short in capturing delayed or complex advertising effects. Real-world advertising often works differently: the effects are delayed and follow varied patterns. To model this, we need a more flexible approach—one that can adapt to the actual impact over time.

## Limitations of Geometric Decay

- **Geometric Adstock**: Assumes a fixed, immediate decline, which doesn’t match situations where advertising takes time to influence sales.

**Formula**:  

_A<sub>t</sub> = X<sub>t</sub> + θ ⋅ A<sub>t-1</sub>_


This is useful for simple cases but doesn’t capture delayed effects.

### Visual 1: Geometric Decay (Traditional Adstock)

![AdstockDecay](https://github.com/user-attachments/assets/0e45e339-7846-4cad-843c-efb41a46429f)
This plot illustrates the simplicity of geometric adstock. Impression peaks during advertising and quickly decreases shortly afterwards. 


## Why Use the Weibull Transformation?

The Weibull distribution offers a flexible alternative that can mimic delayed impacts and various decay patterns in advertising. It introduces two parameters—**shape** (k) and **scale** (λ)—that allow the decay rate to change over time. This flexibility is crucial for real-world data where advertising effects aren’t immediate.

- **Shape (k)**: Controls how quickly or slowly the effect builds and decays. For example:
  - If \( k > 1 \), the impact starts slowly and then decays faster after peaking.
  - If \( k < 1 \), the impact peaks early and decays gradually.

- **Scale (λ)**: Determines when the effect begins. Larger values delay the start, modeling longer-lasting effects.

**Formula**:  

_media_adstocked<sub>ij</sub> = media_raw<sub>ij</sub> + decay_rate<sub>ij</sub> ⋅ media_raw<sub>i-1,j</sub>_


### Visual 2: Weibull Decay (Flexible, Delayed Impact)

![WeibullDecay](https://github.com/user-attachments/assets/fc51cd2e-2597-4fcd-860d-f2818f271e9a)

This plot illustrates the flexibility of the Weibull model. Here, impressions start to rise after the advertisement, peak later, and decay gradually—capturing a more realistic pattern.

## Example R Code for Weibull Simulation

To illustrate Weibull’s flexibility, consider this example where advertising spend begins in week 3, but the impact on sales doesn’t start until later.

```r
# Set seed for reproducibility
set.seed(123)
weeks <- 1:20
advertising_spend <- c(rep(0, 2), rep(100, 18))  # Ad spend starts in week 3
shape_param <- 2
scale_param <- 5

# Weibull CDF function to simulate delayed impact
weibull_adstock <- function(weeks, shape, scale) {
  pweibull(weeks, shape = shape, scale = scale)
}

# Calculate incremental sales using the Weibull CDF and an adjusted curve for a gradual decay
incremental_sales <- advertising_spend * weibull_adstock(weeks - 2, shape_param, scale_param)
incremental_sales <- incremental_sales * (1 - (weeks - 2) / max(weeks - 2))  # Apply a decay adjustment
sales_data <- data.frame(weeks, advertising_spend, incremental_sales)

# Print the data frame
print(sales_data)

# Plot incremental sales over weeks
plot(weeks, incremental_sales, type = "b", col = "purple", pch = 19, 
     xlab = "Weeks", ylab = "Incremental Sales", 
     main = "Weibull-Based Incremental Sales Over Time")
abline(v = 3, col = "blue", lty = 2)  # Indicate the start of advertising with a vertical line
legend("topright", legend = c("Incremental Sales", "Start of Advertising"), 
       col = c("purple", "blue"), lty = c(1, 2), pch = c(19, NA))
```
This code models delayed impact, showing how Weibull can create a realistic curve that rises after a delay and decays gradually—far more flexible than geometric adstock.

## Conclusion

For advertising campaigns where impact unfolds over time, the Weibull transformation provides a better fit than traditional adstock. With its flexible parameters, it allows us to capture delayed and complex decay patterns, making it ideal for campaigns with longer-lasting effects. By adjusting the **shape** and **scale** parameters, the Weibull transformation can model a range of response behaviors, from immediate impacts to gradual, delayed decays. 

In summary:
- **Geometric Adstock**: Works for simple, immediate impacts with steady decline.
- **Weibull Adstock**: Offers flexibility to model real-world, delayed, and non-linear advertising effects.

Whether you choose the CDF for gradual decay or the PDF for capturing lagged effects, Weibull’s flexibility makes it a valuable addition to any marketing analytics toolkit.

