# **[technologies-mac-catalyst] app-structure**

iOS and macOS apps often organize data in similar ways, but they use different controls and visual indicators to help people understand and navigate through the data. When you bring your iOS app to the Mac with Mac Catalyst, plan to spend time making changes to your app’s structure and navigation so that it follows Mac conventions.

Typically, iPad apps use the following UIKit controls to organize their content and features:

- [Split views](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/split-views). A split view enables hierarchical navigation which consists of a two- or three-column interface that shows a primary column, an optional supplementary column, and a secondary pane of content. Frequently, apps use the primary column to create a sidebar-based interface where changes in the sidebar drive changes in the optional supplementary column, which then affect the content in the content pane.
- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars). A tab bar supports flat navigation by displaying top-level categories in a persistent bar at the bottom of the screen.
- [Page controls](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls). A page control displays dots at the bottom of the screen that indicate the position of the current page in a flat list of pages.

**If you use a tab bar in your iPad app, consider using a split view with a sidebar, or a segmented control.** Both items are similar to macOS navigation conventions. To choose between a split view or a segmented control, consider the following:

- A split view with a sidebar displays a list of top-level items, each of which can disclose a list of child items. Using a sidebar streamlines navigation, because users can view each tab’s contents within the sidebar. By using a sidebar on both iPad and Mac, you create a coherent layout that makes it easy for iPad users to start using the Mac app. To help users organize content, a sidebar can offer features such as labels, sorting, and filtering. Additionally, a sidebar can make use of glyphs to differentiate top-level items.
- A segmented control and a tab bar both accommodate similar interactions — such as mutually exclusive selection. In general, using a split view instead of a tab bar works better than a segmented control. However, a segmented control can work well on the Mac if your app uses a flat navigation hierarchy.

Regardless of how you adapt the tab bar, be sure to give people quick access to top-level items — such as an item in the sidebar — through the macOS View menu. For guidance, see [App menus](https://developer.apple.com/design/human-interface-guidelines/technologies/mac-catalyst/user-interaction#app-menus).

**If your app uses a nested top-level navigation structure, think about ways to create a flatter navigation hierarchy.** Many iPad apps that originated on iPhone use deeply nested navigation controllers, making it difficult for people to navigate within the app. When possible, avoid a nested top-level navigation hierarchy. Instead, adopt a split view with a sidebar and create a flatter hierarchy by making use of the additional screen space on iPad and Mac.

**If you use a split view in your Mac app and can’t avoid a deep content hierarchy, include a back button.** If your content hierarchy is deeper than the number of columns supported by the split view, the middle levels between the primary view and the current content pane may not be visible. On iPad, people can use gestures to navigate to a hidden middle level in the content hierarchy. To ensure that people can retrace their steps on the Mac, include a back button in the toolbar and a corresponding navigation item in the View menu.

**If you use a segmented control in your Mac app, place it at the top of the Mac app’s layout.**Mac users are accustomed to a top-down user flow and the bottom of a Mac app’s window isn’t always visible.

**If you use horizontal paging for navigation, offer Mac users specific controls to navigate between pages.** While flicking or dragging laterally with a finger to navigate is easy, holding down a mouse button and dragging laterally is cumbersome. This is especially the case for people who use a mouse without a horizontal scroll wheel. If you support this type of lateral navigation, help people navigate through pages in your Mac app by putting navigation commands into a menu. In addition, display buttons in the toolbar that allow people to navigate to the next or previous page. For example, Stocks in macOS displays both a Back button in the toolbar and Next Story and Previous Story commands in the View menu.

**Add support for tabs.** Users expect macOS apps to let them open documents or other content in a new tab instead of in a new window. In addition, they can use System Settings to prefer tabs over windows. In this case, the system dynamically adds the relevant menu items to an app’s menus, such as View > Show Tab Bar and Window > Show Next Tab.