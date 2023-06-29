# **[components-navigation-and-search] navigation-bars**

## A navigation bar appears at the top of an app screen, enabling navigation through a hierarchy of content.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/navigation-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/navigation-bar-intro-dark_2x.png)

A navigation bar also provides a natural place to display a screen’s title — helping people orient themselves in your app or game — and it can include controls that affect the screen’s content.

macOS doesn’t provide a navigation bar. To enable navigation in a macOS app, you often use a [sidebar](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/sidebars) or a navigation control like a Back button in a [toolbar](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars). Also, you typically display the title of a macOS [window](https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows) in the title bar.

# **Best practices**

**Use the title area to describe the current screen if it provides useful context.** A screen’s title helps people confirm their location as they navigate your app. However, if titling a navigation bar seems redundant, you can leave the title area empty. For example, Notes doesn’t title the current note because the first line of content typically supplies sufficient context. Your app’s name doesn’t provide useful information about the screen or your content hierarchy, so it doesn’t work well as a title.

**Write a concise screen title.** Aim for a word or short phrase that distills the purpose of the screen. Using no more than about 15 characters tends to work well in most screens because it leaves enough room for a back button and optional controls.

**Consider temporarily hiding the navigation bar to provide a more immersive experience.** For example, Photos hides the navigation bar and other interface elements when people view full-screen photos. If you implement this type of behavior, let people restore the navigation bar by tapping the screen or swiping down.

**Use the standard back button.** People know that the standard back button lets them retrace their steps through a hierarchy of information. If you implement a custom back button, make sure it still looks like a back button, behaves as people expect, matches the rest of your interface, and is consistently implemented throughout your app or game. If you replace the system-provided back button chevron with a custom image, you may need to supply a custom mask image, too. For example, iOS uses this mask to animate the button title during transitions.

**Make sure buttons that use text labels have enough room.** If your navigation bar includes more than one text-labeled button, the text of those buttons may appear to run together, making the buttons indistinguishable. Add separation by inserting a fixed-space item between the buttons. For developer guidance, see [UIBarButtonSystemItemFixedSpace](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace).

# **Platform considerations**

*No additional considerations for tvOS. Not supported in macOS.*

# **iOS, iPadOS**

**Consider using a segmented control in a navigation bar to flatten the information hierarchy.** For example, Phone uses a segmented control in the navigation bar of the Recents tab to let people switch between viewing all recent calls or only missed ones. If a design like this makes sense in your app, place a segmented control in the navigation bar only at the top level of the hierarchy, and be sure to create accurate back-button labels for the second-level screens. For guidance, see [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/segmented-controls).

**Use a large title to help people stay oriented as they navigate and scroll.** For example, Phone uses the large title to clarify the active tab, while Music uses large titles to differentiate content areas like albums, artists, playlists, and radio. By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see [prefersLargeTitles](https://developer.apple.com/documentation/uikit/uinavigationbar/2908999-preferslargetitles).

![https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Standard_2x.png](https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Standard_2x.png)

Standard title

![https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Large_2x.png](https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Large_2x.png)

Large title

**Consider hiding the border of a large-title navigation bar to enhance the sense of connection between title and content.** Use caution applying this design to a standard-title navigation bar, though, because the bar’s title and buttons might be harder to distinguish without a visible border. In contrast, you might want to maintain consistency between the primary and secondary views in a Split View on iPad by using the borderless style in both. You can hide the bottom border of a navigation bar by removing the bar’s shadow (the border automatically reappears when people scroll the content area).

# **watchOS**

The navigation bar appears at the top edge of the Apple Watch screen. The system offers space for a title in the leading end of the navigation bar and displays the clock in the trailing end.

The title area can include navigational elements in two cases.

An app that uses hierarchical navigation displays a back button next to the title of a detail screen. You can’t customize the back button icon.

![https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar_hierarchical-ui_2x.png](https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar_hierarchical-ui_2x.png)

In a modal sheet, the system covers the clock and displays the button that dismisses the sheet in the title area.

![https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-modal-sheet_2x.png](https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-modal-sheet_2x.png)

**IMPORTANT**The clock appears in the navigation bar of every nonmodal app screen. You can’t remove the clock, so be sure to account for it in your designs.

The system uses the minimum layout margins to inset both your title and the clock from the edges of the screen, particularly on Apple Watch Series 4 and later (shown below). For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/foundations/layout).

![https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-guides_2x.png](https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-guides_2x.png)