# **[components-layout-and-organization] disclosure-controls**

## Disclosure controls reveal and hide information and functionality related to specific controls or views.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/disclosure-control-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/disclosure-control-intro-dark_2x.png)

# **Best practices**

**Use a disclosure control to hide details until they’re relevant.** Place controls that people are most likely to use at the top of the disclosure hierarchy so they’re always visible, with more advanced functionality hidden by default. This organization helps people first focus on the most essential information without overwhelming them with too many detailed options.

# **Disclosure triangles**

A disclosure triangle shows and hides information and functionality associated with a view or a list of items. For example, Keynote uses a disclosure triangle to show advanced options when exporting a presentation, and the Finder uses disclosure triangles to progressively reveal hierarchy when navigating a folder structure in list view.

• [Collapsed](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls#)
• [Expanded](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-triangle-before_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-triangle-before_2x.png)


A disclosure triangle points inward from the leading edge when its content is hidden and down when its content is visible. Clicking or tapping the disclosure triangle switches between these two states, and the view expands or collapses accordingly to accommodate the content.

**Provide a descriptive label when using a disclosure triangle.** Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”

For developer guidance, see [NSBezelStyleDisclosure](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyledisclosure).

# **Disclosure buttons**

A disclosure button shows and hides functionality associated with a specific control. For example, the macOS Save sheet shows a disclosure button next to the Save As text field. When people click or tap this button, the Save dialog expands to give advanced navigation options for selecting an output location for their document.

• [Collapsed](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls#)
• [Expanded](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-button-before_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/disclosure-controls/images/disclosure-button-before_2x.png)


A disclosure button points down when its content is hidden and up when its content is visible. Clicking or tapping the disclosure button switches between these two states, and the view expands or collapses accordingly to accommodate the content.

**Place a disclosure button near the content that it shows and hides.**Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.

**Use no more than one disclosure button in a single view.** Multiple disclosure buttons add complexity and can be confusing.

For developer guidance, see [NSBezelStyleRoundedDisclosure](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyleroundeddisclosure).

# **Platform considerations**

*No additional considerations for macOS. Not supported in tvOS or watchOS.*

# **iOS, iPadOS**

Disclosure controls are available in iOS and iPadOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) view.