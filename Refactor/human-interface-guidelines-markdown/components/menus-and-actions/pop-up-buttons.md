Pop-up buttons
==============

A pop-up button displays a menu of mutually exclusive options.![A stylized representation of a pop-up button displaying a set of options. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/334ac7588fce25fa319c3ef611eca905/components-pop-up-button-intro@2x.png)

After people choose an item from a pop-up button’s menu, the menu closes, and the button can update its content to indicate the current selection.

[Best practices](/design/human-interface-guidelines/pop-up-buttons#Best-practices)
----------------------------------------------------------------------------------

**Use a pop-up button to present a flat list of mutually exclusive options or states.** A pop-up button helps people make a choice that affects their content or the surrounding view. Use a [pull-down button](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)
 instead if you need to:

* Offer a list of actions
* Let people select multiple items
* Include a submenu

**Provide a useful default selection.** A pop-up button can update its content to identify the current selection, but if people haven’t made a selection yet, it shows the default item you specify. When possible, make the default selection an item that most people are likely to want.

**Give people a way to predict a pop-up button’s options without opening it.** For example, you can use an introductory label or a button label that describes the button’s effect, giving context to the options.

**Consider using a pop-up button when space is limited and you don’t need to display all options all the time.** Pop-up buttons are a space-efficient way to present a wide array of choices.

**If necessary, include a Custom option in a pop-up button’s menu to provide additional items that are useful in some situations.** Offering a Custom option can help you avoid cluttering the interface with items or controls that people need only occasionally. You can also display explanatory text below the list to help people understand how the options work.

[Platform considerations](/design/human-interface-guidelines/pop-up-buttons#Platform-considerations)
----------------------------------------------------------------------------------------------------

*No additional considerations for iOS, macOS, or visionOS. Not supported in tvOS or watchOS.*

### [iPadOS](/design/human-interface-guidelines/pop-up-buttons#iPadOS)

**Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item.** For example, people can quickly choose an option from the pop-up button’s menu without navigating to a detail view. Consider using a pop-up button in this scenario when you have a fairly small, well-defined set of options that work well in a menu.

[Resources](/design/human-interface-guidelines/pop-up-buttons#Resources)
------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/pop-up-buttons#Related)

[Pull-down buttons](/design/human-interface-guidelines/pull-down-buttons)


[Buttons](/design/human-interface-guidelines/buttons)


[Menus](/design/human-interface-guidelines/menus)


#### [Developer documentation](/design/human-interface-guidelines/pop-up-buttons#Developer-documentation)

[`MenuPickerStyle`](/documentation/SwiftUI/MenuPickerStyle)


[`changesSelectionAsPrimaryAction`](/documentation/uikit/uibutton/3752184-changesselectionasprimaryaction)


[`NSPopUpButton`](/documentation/appkit/nspopupbutton)


#### [Videos](/design/human-interface-guidelines/pop-up-buttons#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/4445FCE4-AF6C-435D-BEF8-7A5A73D51270/4954_wide_250x141_1x.jpg) Meet the UIKit button system](https://developer.apple.com/videos/play/wwdc2021/10064) 
[Change log](/design/human-interface-guidelines/pop-up-buttons#Change-log)
--------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| September 14, 2022 | Added a guideline on using a pop-up button in a popover or modal view in iPadOS. |

