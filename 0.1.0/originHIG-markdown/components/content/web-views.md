# **[content] web-views**

## A web view loads and displays rich web content, such as embedded HTML and websites, directly within your app.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/web-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/web-view-intro-dark_2x.png)

For example, Mail uses a web view to show HTML content in messages.

# **Best practices**

**Enable forward and back navigation when appropriate.** Web views support forward and back navigation, but this behavior is disabled by default. If people will use your web view to visit multiple pages, enable forward and back navigation, and provide corresponding controls to initiate these features.

**Avoid using a web view to build a web browser.** Using a web view to let people briefly access a website without leaving the context of your app is fine, but Safari is the primary way people browse the web. Attempting to replicate the functionality of Safari in your app is unnecessary and discouraged.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, or macOS. Not supported in tvOS or watchOS.*