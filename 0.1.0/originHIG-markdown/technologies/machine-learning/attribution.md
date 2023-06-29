# **[technologies-machine-learning] attribution**

An attribution expresses the underlying basis or rationale for a result, without explaining exactly how a model works. Depending on the design of your app, you might want to use attributions to impart transparency and give people insight into your results. For example, if your app suggests books for people to read, you might use an attribution like “Because you’ve read mysteries” when you suggest books in the “thrillers” category.

![https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/attribution_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/images/attribution_2x.png)

To help you decide whether to include attributions in your app, consider how you want them to affect people. For example, do you want attributions to:

- Encourage people to change what they do in your app?
- Minimize the impact of [mistakes](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/mistakes)?
- Help people build a mental model of your feature?
- Promote trust in your app over time?

**Consider using attributions to help people distinguish among results.** For example, if you present a set of results as [multiple options](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/multiple-options), including attributions can help people choose an option based on their understanding of the premise that led to it, such as "New books by authors you’ve read."

**Avoid being too specific or too general.** Overly specific attributions can make people feel like they have to do additional work to interpret the results, whereas overly general attributions typically don’t provide useful information. In apps that make content recommendations, general attributions can make people feel like your app is not treating them as individuals, but overly specific attributions can make people think that your app is watching them too closely. The best attributions strike a balance between these extremes.

**Keep attributions factual and based on objective analysis.** To be useful, an attribution should help people reason about a result; you don’t want to provoke an emotional response. Don’t provide an attribution that implies understanding or judgment of people’s emotions, preferences, or beliefs. For example, an app that recommends new content to people should use an attribution like "Because you’ve read nonfiction" instead of an attribution like "Because you love nonfiction."

**In general, avoid technical or statistical jargon.** In most situations, using percentages, statistics, and other technical jargon doesn’t help people assess the results you provide. The exception to this is when the result itself is of a statistical or technical nature, such as information in the areas of weather, sports, polling and election results, or scientific data.