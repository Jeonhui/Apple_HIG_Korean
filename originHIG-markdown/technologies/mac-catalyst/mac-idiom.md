# **[technologies-mac-catalyst] mac-idiom**

When you first create your Mac app with Mac Catalyst, Xcode defaults to the iPad idiom. With this setting, the system ensures that your Mac app appears consistent with the macOS display environment without requiring significant changes to the app’s layout. However, text and graphics may appear slightly less detailed.

After you’ve spent time making your app feel at home on the Mac, consider switching to the Mac idiom. With this setting, text and artwork renders in more detail, and some interface elements and views take on an even more Mac-like appearance.

Apps that display a lot of text, detailed artwork, or use animations are most likely to benefit from this setting. Nevertheless, adopting the Mac idiom typically requires spending additional time to update your Mac app’s layout.

# **Review differences between the iPad and the Mac idiom**

One of the main differences between the iPad idiom and the Mac idiom is the appearance of iOS views and text. Specifically, iOS views and text scale down to 77% in macOS when you use the iPad idiom. When you adopt the Mac idiom to further optimize your Mac app, iOS views render at 100% of their size, and text and graphics appear more detailed.

Below are two versions of an image asset. One version illustrates how the asset appears when you use the iPad idiom, and the other version shows how the asset appears when you adopt the Mac idiom. Both are zoomed in to show how the image renders with more details when you adopt the Mac idiom.

• [iPad idiom](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/mac-idiom#)
• [Mac idiom](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/mac-idiom#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/ipad-idiom_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/images/ipad-idiom_2x.png)


In addition to displaying unscaled text and images, selecting the Mac idiom further optimizes your app to provide the best possible experience on the Mac; for example:

- Some iOS interface elements and views like buttons or the color well take on a more Mac-like appearance.
- An iOS switch becomes a checkbox in macOS.
- Controls and interface elements in macOS take advantage of wider macOS windows and use more horizontal padding and often take up more space.
- Graphics-intensive apps may see improved performance and lower power consumption.

**When you adopt the Mac idiom, thoroughly audit your app’s layout and plan to make changes to it.** In addition, you may need to use an asset catalog that contains your Mac app’s assets instead of reusing the asset catalog that contains your iPad app’s assets.

**Limit your appearance customizations to standard macOS appearance customizations that overlap with those available in iOS.** Not all appearance customizations available to iOS controls are available to macOS controls.

**DEVELOPER NOTE**When you adopt the Mac idiom, the unscaled views and interface elements report different metrics, often resulting in a significant amount of additional work. To reduce the amount of work, avoid fixed font, view, or layout sizes. Additionally, make sure any appearance customizations you use are available in macOS. For developer guidance, see [Choosing a user interface idiom for your Mac app](https://developer.apple.com/documentation/uikit/mac_catalyst/choosing_a_user_interface_idiom_for_your_mac_app)