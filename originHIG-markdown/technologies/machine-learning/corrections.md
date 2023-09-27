# **[technologies-machine-learning] corrections**

People use corrections to fix mistakes that apps make. For example, if a photo app automatically crops a photo in a way people don’t like, they can correct the mistake by cropping the photo in a different way.

**Give people familiar, easy ways to make corrections.** When your app makes a mistake, you don’t want people to be confused about how to correct it. You can avoid causing confusion by showing the steps your app takes as it performs the automated task. For example, Photos highlights the controls it uses to auto-crop a photograph so that people can use the same controls to refine or undo the results.

**Provide immediate value when people make a correction.** Reward people’s effort by instantly displaying corrected content, especially when the feature is critical or you’re responding to direct user input. Also, be sure to persist the updates so people don’t have to make the same corrections again.

**Let people correct their corrections.** Sometimes, people make a correction without realizing that they’ve made a mistake. As you do with all corrections, respond immediately to an updated correction and persist the update.

**Always balance the benefits of a feature with the effort required to make a correction.**People may not mind when a feature that automates a task makes a mistake, but they’re likely to stop using the feature if it seems easier to perform the task themselves.

**Never rely on corrections to make up for low-quality results.** Although corrections can reduce the impact of a mistake, depending on them may erode people’s trust in your app and reduce the value of your feature.

**Learn from corrections when it makes sense.** A correction is a type of [implicit feedback](https://developer.apple.com/design/human-interface-guidelines/technologies/machine-learning/implicit-feedback) that can give you valuable information about ways your app doesn’t meet people’s expectations. Before you use a correction to update your models, make sure that the correction will lead to higher quality results.

**When possible, use guided corrections instead of freeform corrections.** Guided corrections suggest specific alternatives, so they require less user effort; freeform corrections don’t suggest specific alternatives, so they require more input from people. An example of guided correction is a speech-to-text feature that gives people a list of alternative text completions from which to choose. In contrast, Photos offers freeform correction so that people can adjust the auto-cropping of a photo as they see fit. If it makes sense in your app, you can support a combination of guided and freeform corrections.