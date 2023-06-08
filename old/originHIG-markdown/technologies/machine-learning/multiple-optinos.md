# **[technologies-machine-learning] multiple-optinos**

Depending on the design of your feature, it might work best to present a single result or multiple results from which people can choose. Providing multiple options can give people a greater sense of control and can help bridge the gap between your model’s predictions and what people actually want. Multiple options can also encourage people to have realistic expectations about the types of results your app generates.

![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/multiple-options_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/multiple-options_2x.png)

You might present multiple options to people in the following contexts:

- Suggested options, a proactive feature that suggests content to people based on the their past interactions. For example, For You recommendations from Apple Music.
- Requested options, a reactive feature that suggests potential next steps to people based on their recent actions. For example, Quick Type suggestions.
- Corrections, which are actions people take to fix mistakes your app has made when it’s acting on their behalf. For example, the Photos Auto-Crop feature.

**Prefer diverse options.** When possible, balance the accuracy of a response with the diversity of multiple options. For example, Apple Maps generally suggests more than one route to a destination, such as a route without tolls, a scenic route, or a route that uses highways. Providing different types of options helps people choose the one that they prefer and can also suggest new items that might interest them.

**In general, avoid providing too many options.** People must evaluate each option before making a choice, so more options increases cognitive load. When possible, list options on one screen so people don’t have to scroll to find the right one.

**List the most likely option first.** When you know how your [confidence](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/confidence) values correlate with the quality of your results, you might use them to rank the options. You might also consider using contextual information, such as the time of day or the current location, to help you determine the most likely option. If it makes sense in your app, select the first option by default so people can quickly achieve their goals without reading through every option.

**Make options easy to distinguish and choose.** For example, in a routing app, people often need to make route choices quickly to avoid going the wrong way. When options look similar, help people distinguish between them by providing a brief description of each one and taking particular care to highlight the differences. In cases where there are too many options to display in a single view, such as with content recommendations, consider grouping options in categories that people can scan rapidly.

**Learn from selections when it makes sense.** People give you [implicit feedback](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/implicit-feedback) every time they make a selection. When it doesn’t adversely affect the user experience, use this feedback to refine the options you provide and increase the chance that you’ll present the most likely option first. In general, continuing to offer incorrect results is likely to decrease people’s trust in the quality of your app’s predictions.