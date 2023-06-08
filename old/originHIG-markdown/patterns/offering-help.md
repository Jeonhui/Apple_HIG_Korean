# **[patterns] offering-help**

# Although the most effective experiences are approachable and intuitive, you can provide contextual help when necessary.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-offering-help-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-offering-help-intro-dark_2x.png)

# **Best practices**

**Let the tasks you enable inform the types of help people might need.** For example, you might help people perform simple, one- or two-step tasks by displaying an inline view that succinctly describes the task. In contrast, if your app or game enables complex or multistep tasks you might want to provide a tutorial that teaches people how to accomplish larger goals. In general, directly relate the help you provide to the precise action or task people are doing right now and make it easy for people to dismiss or avoid the help if they don’t need it.

**Use relevant and consistent language and images in your help content.** Always make sure guidance is appropriate for the current context. For example, if someone’s using the Siri Remote with your tvOS experience, don’t show tips or images that feature a game controller. Also be sure the terms and descriptions you use are consistent with the platform. For example, don’t write copy that tells people to click a button on an iPhone or tap a menu item on a Mac.

**Make sure all help content is inclusive.** For guidance, see [Inclusion](https://developer.apple.com/design/human-interface-guidelines/foundations/inclusion/).

**Avoid bloating your help content by explaining how standard components or patterns work.** Instead, focus on describing the specific action or task that a standard element enables in your app or game. If your experience introduces a unique control or expects people to use an input device in a nonstandard way — such as holding the Siri Remote rotated 90 degrees — orient people quickly, preferring animation or graphics to educate instead of a lengthy description.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, tvOS, or watchOS.*

# **macOS**

A help tag (also called a *tooltip*) displays a small, transient view that briefly describes how to use a component in the interface. In apps that run on a Mac — including iPhone and iPad apps — help tags can appear after the pointer hovers briefly over an element.

**Focus only on the control that’s directly beneath the pointer.** When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.

**Describe the action or task the control initiates.** It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”

**Be brief.** As much as possible, limit tag content to a maximum of 60 to 75 characters (note that localization often changes the length of text). To make a description brief and direct, consider using a sentence fragment and omitting articles. If you need a lot of text to describe a control, consider simplifying your interface design.

**In general, avoid naming or referring to the component.** A help tag appears directly over the control, which usually provides sufficient context. Avoid defining a tag that does nothing but repeat the control’s title or label.

**Consider offering context-sensitive help tags.** For example, you could provide different text for a control’s different states.