# **[technologies-machine-learning] machine-learning-roles**

# **Defining the role of machine learning in your app**

Machine learning systems vary widely, and the ways an app can use machine learning vary widely, too. As you approach the design of your app, think about how its features use machine learning in each of the following areas.

# **Critical or complementary**

If an app can still work without the feature that machine learning enables, machine learning is complementary to the app; otherwise, it’s a critical dependency. For example:

- The keyboard uses machine learning to provide QuickType suggestions. Because the keyboard still works without these suggestions, machine learning plays a complementary role in the app.
- Face ID relies on machine learning to enable accurate face recognition. Without machine learning, Face ID would not work.

In general, the more critical an app feature is, the more people need accurate and reliable results. On the other hand, if a complementary feature delivers results that aren’t always of the highest quality, people may be more forgiving.

# **Private or public**

Machine learning results depend on data. To make good design decisions, you need to know as much as possible about the types of data your app feature needs. In general, the more sensitive the data, the more serious the consequences of inaccurate or unreliable results. For example:

- If a health app misinterprets data and incorrectly recommends a visit to the doctor, people are likely to experience anxiety and may lose trust in the app.
- If a music app misinterprets data and recommends an artist that people don’t like, they’re likely to view the result as an inconsequential mistake.

As with critical app features, features that use sensitive data should prioritize accuracy and reliability. Regardless of the sensitivity of the data, all apps must protect user privacy at all times.

# **Proactive or reactive**

A *proactive* app feature provides results without people requesting it to do so. Proactive features can prompt new tasks and interactions by providing unexpected, sometimes serendipitous results. In contrast, a *reactive* app feature provides results when people ask for them or when they take certain actions. Reactive features typically help people as they perform their current task. For example:

- QuickType suggests words in reaction to what people type.
- Siri Suggestions can proactively suggest a shortcut based on people’s recent routines.

Because people don’t ask for the results that a proactive feature provides, they may have less tolerance for low-quality information. To reduce the possibility that people will find proactive results intrusive or irrelevant, you may need to use additional data for the feature.

# **Visible or invisible**

Apps may use machine learning to support visible or invisible features. People are usually aware of visible app features because such features tend to offer suggestions or choices that people view and interact with. For example, a visible keyboard feature tries to guess the word that people are typing and presents the most likely words in a list from which people choose.

As the name suggests, an invisible feature provides results that aren’t obvious to people. For example, the keyboard learns how people type over time so it can optimize the tap area for each key and help them make fewer typing mistakes. Because this app feature improves the typing experience without requiring people to make choices, many people aren’t aware that the feature exists.

People’s impression of the reliability of results can differ depending on whether a feature is visible or invisible. With a visible feature, people form an opinion about the feature’s reliability as they choose from among its results. It’s harder for an invisible feature to communicate its reliability — and potentially receive feedback — because people may not be aware of the feature at all.

# **Dynamic or static**

All machine learning models can improve, but some improve dynamically, as people interact with the app feature, and others improve offline and affect the feature only when the app updates. For example:

- Face ID improves dynamically as people’s faces gradually change over time.
- Photos improves its object recognition capabilities with every new iOS release.

In addition to the frequency of app updates, static or dynamic improvements can affect other parts of the user experience, too. For example, dynamic features often incorporate forms of [calibration](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/calibration)and feedback (either [implicit](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/implicit-feedback) or [explicit](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/explicit-feedback)), whereas static features may not.