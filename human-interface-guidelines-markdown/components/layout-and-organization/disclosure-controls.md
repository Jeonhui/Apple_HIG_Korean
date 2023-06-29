Disclosure controls
===================

Disclosure controls reveal and hide information and functionality related to specific controls or views.![A stylized representation of collapsed and expanded disclosure buttons. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/d9f8c2e1696219ad884582186a447524/components-disclosure-control-intro@2x.png)

[Best practices](/design/human-interface-guidelines/disclosure-controls#Best-practices)
---------------------------------------------------------------------------------------

**Use a disclosure control to hide details until they’re relevant.** Place controls that people are most likely to use at the top of the disclosure hierarchy so they’re always visible, with more advanced functionality hidden by default. This organization helps people first focus on the most essential information without overwhelming them with too many detailed options.

[Disclosure triangles](/design/human-interface-guidelines/disclosure-controls#Disclosure-triangles)
---------------------------------------------------------------------------------------------------

A disclosure triangle shows and hides information and functionality associated with a view or a list of items. For example, Keynote uses a disclosure triangle to show advanced options when exporting a presentation, and the Finder uses disclosure triangles to progressively reveal hierarchy when navigating a folder structure in list view.

* [Collapsed](#)
* [Expanded](#)
![A screenshot of the Keynote app's export to PDF dialog in macOS. The dialog includes a closed disclosure triangle that expands to reveal a set of advanced options.](https://docs-assets.developer.apple.com/published/940fe48b19aaa4a4e76e704e9f506576/disclosure-triangle-before@2x.png)

![A screenshot of the Keynote app's export to PDF dialog in macOS. The dialog includes an expanded disclosure triangle that collapses to hide a set of advanced options.](https://docs-assets.developer.apple.com/published/1b10c2e496c8d0dca74d85d841d67e35/disclosure-triangle-after@2x.png)

A disclosure triangle points inward from the leading edge when its content is hidden and down when its content is visible. Clicking or tapping the disclosure triangle switches between these two states, and the view expands or collapses accordingly to accommodate the content.

**Provide a descriptive label when using a disclosure triangle.** Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”

For developer guidance, see [`NSBezelStyleDisclosure`](/documentation/appkit/nsbezelstyle/nsbezelstyledisclosure)
.

[Disclosure buttons](/design/human-interface-guidelines/disclosure-controls#Disclosure-buttons)
-----------------------------------------------------------------------------------------------

A disclosure button shows and hides functionality associated with a specific control. For example, the macOS Save sheet shows a disclosure button next to the Save As text field. When people click or tap this button, the Save dialog expands to give advanced navigation options for selecting an output location for their document.

* [Collapsed](#)
* [Expanded](#)
![A screenshot of a collapsed save dialog in macOS. The dialog includes a closed disclosure button that expands the dialog to reveal additional options.](https://docs-assets.developer.apple.com/published/41fe1293ec292d9ad86a405eea10ec9f/disclosure-button-before@2x.png)

![A screenshot of an expanded save dialog in macOS. The dialog includes an open disclosure button that collapses the dialog to hide some options.](https://docs-assets.developer.apple.com/published/4a9d1b5b20d1802f6dff607c63997899/disclosure-button-after@2x.png)

A disclosure button points down when its content is hidden and up when its content is visible. Clicking or tapping the disclosure button switches between these two states, and the view expands or collapses accordingly to accommodate the content.

**Place a disclosure button near the content that it shows and hides.** Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.

**Use no more than one disclosure button in a single view.** Multiple disclosure buttons add complexity and can be confusing.

For developer guidance, see [`NSBezelStyleRoundedDisclosure`](/documentation/appkit/nsbezelstyle/nsbezelstyleroundeddisclosure)
.

[Platform considerations](/design/human-interface-guidelines/disclosure-controls#Platform-considerations)
---------------------------------------------------------------------------------------------------------

*No additional considerations for macOS. Not supported in tvOS or watchOS.*

### [iOS, iPadOS, visionOS](/design/human-interface-guidelines/disclosure-controls#iOS-iPadOS-visionOS)

Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [`DisclosureGroup`](/documentation/SwiftUI/DisclosureGroup)
 view.

[Resources](/design/human-interface-guidelines/disclosure-controls#Resources)
-----------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/disclosure-controls#Related)

[Outline views](/design/human-interface-guidelines/outline-views)


[Lists and tables](/design/human-interface-guidelines/lists-and-tables)


[Buttons](/design/human-interface-guidelines/buttons)


#### [Developer documentation](/design/human-interface-guidelines/disclosure-controls#Developer-documentation)

[`DisclosureGroup`](/documentation/SwiftUI/DisclosureGroup)


[`NSBezelStyleRoundedDisclosure`](/documentation/appkit/nsbezelstyle/nsbezelstyleroundeddisclosure)


[`NSBezelStyleDisclosure`](/documentation/appkit/nsbezelstyle/nsbezelstyledisclosure)


#### [Videos](/design/human-interface-guidelines/disclosure-controls#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/49/1636D358-5C36-4027-B204-81FFE4D05B7D/3455_wide_250x141_1x.jpg) Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031) 
