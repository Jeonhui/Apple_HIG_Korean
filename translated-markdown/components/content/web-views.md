# **[content] web-views**

## A web view loads and displays rich web content, such as embedded HTML and websites, directly within your app.
> 웹 보기는 내장된 HTML 및 웹 사이트와 같은 풍부한 웹 콘텐츠를 앱 내에 직접 로드하고 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/web-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/web-view-intro-dark_2x.png)

For example, Mail uses a web view to show HTML content in messages.
> 예를 들어, 메일은 웹 보기를 사용하여 메시지의 HTML 내용을 표시합니다.
>




# **Best practices**

**Enable forward and back navigation when appropriate.** Web views support forward and back navigation, but this behavior is disabled by default. If people will use your web view to visit multiple pages, enable forward and back navigation, and provide corresponding controls to initiate these features.
> 적절한 경우 정방향 및 역방향 탐색을 사용하도록 설정합니다. 웹 보기는 정방향 및 역방향 탐색을 지원하지만 이 동작은 기본적으로 비활성화되어 있습니다. 다른 사용자가 웹 보기를 사용하여 여러 페이지를 방문할 경우 앞으로 및 뒤로 탐색을 활성화하고 이러한 기능을 시작하기 위한 해당 컨트롤을 제공합니다.
>




**Avoid using a web view to build a web browser.** Using a web view to let people briefly access a website without leaving the context of your app is fine, but Safari is the primary way people browse the web. Attempting to replicate the functionality of Safari in your app is unnecessary and discouraged.
> 웹 보기를 사용하여 웹 브라우저를 만들지 마십시오. 웹 보기를 사용하여 앱의 컨텍스트를 벗어나지 않고 웹 사이트에 잠시 액세스할 수 있도록 하는 것은 좋지만 Safari는 사람들이 웹을 탐색하는 주된 방법입니다. 앱에서 Safari의 기능을 복제하려는 시도는 불필요하고 권장되지 않습니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or macOS. Not supported in tvOS or watchOS.*
> iOS, iPadOS 또는 macOS에 대한 추가 고려 사항은 없습니다. tvOS 또는 시계에서 지원되지 않음OS.
>



