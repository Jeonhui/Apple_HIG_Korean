# **[components-selection-and-input] toggles**

## A toggle lets people choose between a pair of opposing states, like on and off, using a different appearance to indicate each state.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toggles-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/toggles-intro-dark_2x.png)

Different platforms can support various toggle [styles](https://developer.apple.com/documentation/swiftui/togglestyle). For example, iOS, iPadOS, macOS, and watchOS support the switch toggle style, whereas only macOS supports the checkbox style.

In addition, all platforms support buttons that enable toggle behavior by using a different appearance for each state.

# **Best practices**

**Use a toggle to help people choose between two opposing values that affect the state of content or a view.** A toggle always lets people manage the state of something, so if you need to enable other types of actions — such as choosing from a list of items — use a different component, like a [pop-up button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pop-up-buttons).

**Clearly identify the setting, view, or content the toggle affects.** In general, the surrounding context provides enough information for people to understand what they’re turning on or off. In some cases, often in macOS apps, you can also supply a label to describe the state the toggle controls. If you use a button that behaves like a toggle, you generally use an interface icon that communicates its purpose, and you update its appearance — typically by changing the background — based on the current state.

**Make sure the visual differences in a toggle’s state are obvious.** For example, you might add or remove a color fill, show or hide the background shape, or change the inner details you display — like a checkmark or dot — to show that a toggle is on or off. Avoid relying solely on different colors to communicate state, because not everyone can perceive the differences.

# **Platform considerations**

*No additional considerations for tvOS or watchOS.*

# **iOS, iPadOS**

**Use the switch toggle style only in a list row.** You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.

**Change the default color of a switch only if necessary.** The default green color tends to work well in most cases, but you might want to use your app’s accent color instead. Be sure to use a color that provides enough contrast with the uncolored appearance to be perceptible.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/switches-default_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/switches-default_2x.png)

**Outside of a list, use a button that behaves like a toggle, not a switch.**Avoid supplying a label that explains the button’s purpose. The interface icon you create — combined with the alternative background appearances you supply — help people understand what the button does. For developer guidance, see [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/3752184-changesselectionasprimaryaction/).

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-on_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-on_2x.png)

Calendar displays a solid background shape behind the toggle’s symbol to indicate that the day’s events are visible.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-off_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/toggle-button-off_2x.png)

Calendar removes the solid background shape from the toggle to indicate that the day’s events are hidden.

# **macOS**

In addition to the switch toggle style, macOS supports the checkbox style and also defines radio buttons that can provide similar behaviors.

**Use switches, checkboxes, and radio buttons in the window body, not the window frame.** In particular, avoid using these components in a toolbar or status bar.

### **Switches**

**Avoid using a switch to control a single detail or a minor setting.** A switch has more visual weight than a checkbox, so it looks better when it controls more functionality than a checkbox typically does. For example, you might use a switch to let people turn on or off a group of settings, instead of just one setting.

**In general, don't replace a checkbox with a switch.** If you're already using a checkbox in your interface, it's probably best to keep using it.

### **Checkboxes**

A checkbox is a small square button that’s empty when the button is off, contains a checkmark when the button is on, and can contain a dash when the button’s state is mixed. Unless a checkbox appears in a checklist, a descriptive label follows the button.

**Use a checkbox instead of a switch if you need to present a hierarchy of settings.** The visual style of checkboxes helps them align well and communicate grouping. By using alignment — generally along the leading edge of the checkboxes — and indentation, you can show dependencies, such as when the state of a checkbox governs the state of subordinate checkboxes.

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-alignment.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-alignment.svg)

**Consider using radio buttons if you need to present a set of more than two mutually exclusive options.** When people need to choose from options in addition to just “on” or “off,” using multiple radio buttons can help you clarify each option with a unique label.

**Consider using a label to introduce a group of checkboxes if their relationship isn't clear.** Describe the set of options, and align the label’s baseline with the first checkbox in the group.

**Accurately reflect a checkbox’s state in its appearance.** A checkbox can be selected, deselected, or mixed. If you use a checkbox to globally enable and disable multiple subordinate checkboxes, show a mixed state when the subordinate checkboxes have different states. For example, you might need to present a text-style setting that turns all styles on or off, but also lets people choose a subset of individual style settings like bold, italic, or underline. For developer guidance, see [allowsMixedState](https://developer.apple.com/documentation/appkit/nsbutton/1528670-allowsmixedstate).

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-deselected.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-deselected.svg)

Deselected

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-selected.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-selected.svg)

Selected

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-mixed.svg](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/toggles/images/checkbox-mixed.svg)

Mixed

### **Radio buttons**

A radio button is a small, circular button followed by a label. Typically displayed in groups of two to five, radio buttons present a set of mutually exclusive choices.

A radio button’s state is either on (a filled circle) or off (an empty circle). Although a radio button can also display a mixed state (indicated by a dash), this state is rarely useful because you can communicate multiple states by using additional radio buttons. If you need to show that a setting or item has a mixed state, consider using a checkbox instead.

**Prefer a set of radio buttons to present mutually exclusive options.** If you need to let people choose multiple options in a set, use checkboxes instead.

**Avoid listing too many radio buttons in a set.** A long list of radio buttons takes up a lot of space in the interface and can be overwhelming. If you need to present more than about five options, consider using a component like a [pop-up button](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/pop-up-buttons) instead.

**To present a single setting that can be on or off, prefer a checkbox.**Although a single radio button can also turn something on or off, the presence or absence of the checkmark in a checkbox can make the current state easier to understand at a glance. In rare cases where a single checkbox doesn’t clearly communicate the opposing states, you can use a pair of radio buttons, each with a label that specifies the state it controls.

**Use consistent spacing when you display radio buttons horizontally.**Measure the space needed to accommodate the longest button label, and use that measurement consistently.