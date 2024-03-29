Toggles
=======

A toggle lets people choose between a pair of opposing states, like on and off, using a different appearance to indicate each state.![A stylized representation of two labeled switch controls. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/9ba7467e23a05b9a4180286b3cf2bb3b/components-toggles-intro@2x.png)

A toggle can have various styles, such as switch and checkbox, and different platforms can use these styles in different ways. For guidance, see [Platform considerations](/design/human-interface-guidelines/toggles#Platform-considerations)
.

In addition to toggles, all platforms also support buttons that behave like toggles by using a different appearance for each state. For developer guidance, see [`ToggleStyle`](/documentation/SwiftUI/ToggleStyle)
.

[Best practices](/design/human-interface-guidelines/toggles#Best-practices)
---------------------------------------------------------------------------

**Use a toggle to help people choose between two opposing values that affect the state of content or a view.** A toggle always lets people manage the state of something, so if you need to support other types of actions — such as choosing from a list of items — use a different component, like a [pop-up button](/design/human-interface-guidelines/pop-up-buttons)
.

**Clearly identify the setting, view, or content the toggle affects.** In general, the surrounding context provides enough information for people to understand what they’re turning on or off. In some cases, often in macOS apps, you can also supply a label to describe the state the toggle controls. If you use a button that behaves like a toggle, you generally use an interface icon that communicates its purpose, and you update its appearance — typically by changing the background — based on the current state.

**Make sure the visual differences in a toggle’s state are obvious.** For example, you might add or remove a color fill, show or hide the background shape, or change the inner details you display — like a checkmark or dot — to show that a toggle is on or off. Avoid relying solely on different colors to communicate state, because not everyone can perceive the differences.

[Platform considerations](/design/human-interface-guidelines/toggles#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for tvOS, visionOS, or watchOS.*

### [iOS, iPadOS](/design/human-interface-guidelines/toggles#iOS-iPadOS)

**Use the switch toggle style only in a list row.** You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.

**Change the default color of a switch only if necessary.** The default green color tends to work well in most cases, but you might want to use your app’s accent color instead. Be sure to use a color that provides enough contrast with the uncolored appearance to be perceptible.

![An illustration that represents Sound and Haptics settings on iPhone in which one switch is off and one switch is on.](https://docs-assets.developer.apple.com/published/f09ece0fccaecc2f1cce9038a5574b76/switches-default@2x.png)

**Outside of a list, use a button that behaves like a toggle, not a switch.** Avoid supplying a label that explains the button’s purpose. The interface icon you create — combined with the alternative background appearances you supply — help people understand what the button does. For developer guidance, see [`changesSelectionAsPrimaryAction`](/documentation/uikit/uibutton/3752184-changesselectionasprimaryaction)
.

![A screenshot of the Calendar app on iPhone, showing the current month in the top half of the screen and today’s event view in the bottom half.](https://docs-assets.developer.apple.com/published/6d7617dcfdd87ad24639952087a9a8e9/toggle-button-on@2x.png)Calendar displays a solid background shape behind the toggle’s symbol to indicate that the day’s events are visible.![A screenshot of the Calendar app on iPhone, showing a month view that begins with the current month followed by the first two weeks of the next month.](https://docs-assets.developer.apple.com/published/da7e9f6190f755d15301efcbaece4323/toggle-button-off@2x.png)Calendar removes the solid background shape from the toggle to indicate that the day’s events are hidden.### [macOS](/design/human-interface-guidelines/toggles#macOS)

In addition to the switch toggle style, macOS supports the checkbox style and also defines radio buttons that can provide similar behaviors.

**Use switches, checkboxes, and radio buttons in the window body, not the window frame.** In particular, avoid using these components in a toolbar or status bar.

#### [Switches](/design/human-interface-guidelines/toggles#Switches)

**Avoid using a switch to control a single detail or a minor setting.** A switch has more visual weight than a checkbox, so it looks better when it controls more functionality than a checkbox typically does. For example, you might use a switch to let people turn on or off a group of settings, instead of just one setting.

**In general, don’t replace a checkbox with a switch.** If you’re already using a checkbox in your interface, it’s probably best to keep using it.

#### [Checkboxes](/design/human-interface-guidelines/toggles#Checkboxes)

A checkbox is a small square button that’s empty when the button is off, contains a checkmark when the button is on, and can contain a dash when the button’s state is mixed. Unless a checkbox appears in a checklist, a descriptive label follows the button.

**Use a checkbox instead of a switch if you need to present a hierarchy of settings.** The visual style of checkboxes helps them align well and communicate grouping. By using alignment — generally along the leading edge of the checkboxes — and indentation, you can show dependencies, such as when the state of a checkbox governs the state of subordinate checkboxes.

![An illustration showing a layout that includes two levels of checkboxes.](https://docs-assets.developer.apple.com/published/ea2e9ff93f295143ab019e7d7e27e775/checkbox-alignment@2x.png)

**Consider using radio buttons if you need to present a set of more than two mutually exclusive options.** When people need to choose from options in addition to just “on” or “off,” using multiple radio buttons can help you clarify each option with a unique label.

**Consider using a label to introduce a group of checkboxes if their relationship isn’t clear.** Describe the set of options, and align the label’s baseline with the first checkbox in the group.

**Accurately reflect a checkbox’s state in its appearance.** A checkbox can be in a selected, deselected, or mixed state. If you use a checkbox to globally turn on and off multiple subordinate checkboxes, show a mixed state when the subordinate checkboxes have different states. For example, you might need to present a text-style setting that turns all styles on or off, but also lets people choose a subset of individual style settings like bold, italic, or underline. For developer guidance, see [`allowsMixedState`](/documentation/appkit/nsbutton/1528670-allowsmixedstate)
.

![A partial screenshot that shows a deselected checkbox, which looks like a small rounded square with no fill.](https://docs-assets.developer.apple.com/published/0f4f21bb112cccefe8b69712d7846ef7/checkbox-deselected@2x.png)Deselected![A partial screenshot that shows a selected checkbox, which looks like a small rounded square with dark fill and a white checkmark.](https://docs-assets.developer.apple.com/published/dc5e5f6c1ef897b580737e7adf13c597/checkbox-selected@2x.png)Selected![A partial screenshot that shows a mixed checkbox, which looks like a small rounded square with dark fill and a white hyphen.](https://docs-assets.developer.apple.com/published/3f7c4b9388cf0960c265d473798ec78c/checkbox-mixed@2x.png)Mixed#### [Radio buttons](/design/human-interface-guidelines/toggles#Radio-buttons)

A radio button is a small, circular button followed by a label. Typically displayed in groups of two to five, radio buttons present a set of mutually exclusive choices.

A radio button’s state is either on (a filled circle) or off (an empty circle). Although a radio button can also display a mixed state (indicated by a dash), this state is rarely useful because you can communicate multiple states by using additional radio buttons. If you need to show that a setting or item has a mixed state, consider using a checkbox instead.

**Prefer a set of radio buttons to present mutually exclusive options.** If you need to let people choose multiple options in a set, use checkboxes instead.

**Avoid listing too many radio buttons in a set.** A long list of radio buttons takes up a lot of space in the interface and can be overwhelming. If you need to present more than about five options, consider using a component like a [pop-up button](/design/human-interface-guidelines/pop-up-buttons)
 instead.

**To present a single setting that can be on or off, prefer a checkbox.** Although a single radio button can also turn something on or off, the presence or absence of the checkmark in a checkbox can make the current state easier to understand at a glance. In rare cases where a single checkbox doesn’t clearly communicate the opposing states, you can use a pair of radio buttons, each with a label that specifies the state it controls.

**Use consistent spacing when you display radio buttons horizontally.** Measure the space needed to accommodate the longest button label, and use that measurement consistently.

[Resources](/design/human-interface-guidelines/toggles#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/toggles#Related)

[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/toggles#Developer-documentation)

[`Toggle`](/documentation/SwiftUI/Toggle)


[`UISwitch`](/documentation/uikit/uiswitch)


[`NSButton.ButtonType.toggle`](/documentation/appkit/nsbutton/buttontype/toggle)


[`NSSwitch`](/documentation/appkit/nsswitch)


