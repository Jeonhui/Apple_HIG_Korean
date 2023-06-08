# **[patterns] settings**

# People expect apps and games to just work, but they also appreciate having ways to customize the experience to fit their needs.
> 사람들은 앱과 게임이 그저 작동하기를 기대하지만, 그들은 또한 그들의 필요에 맞게 경험을 사용자 정의할 수 있는 방법을 갖는 것을 높이 평가한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-settings-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-settings-intro-dark_2x.png)

When it makes sense, you can offer context-specific settings within your app or game so people don’t have to leave their current task to make adjustments. If you also offer settings that affect the overall app or game, you can provide a custom settings area. In iOS, iPadOS, macOS, and tvOS, the system provides a Settings app that can include some app-specific options.
> 이 경우 앱이나 게임 내에서 컨텍스트별 설정을 제공하므로 사용자가 조정하기 위해 현재 작업을 떠날 필요가 없습니다. 전체 앱이나 게임에 영향을 미치는 설정도 제공하는 경우 사용자 지정 설정 영역을 제공할 수 있습니다. iOS, iPadOS, macOS 및 tvOS에서 시스템은 일부 앱별 옵션을 포함할 수 있는 설정 앱을 제공합니다.
>




# **Best practices**

**As much as possible, let people modify task-specific options without going to a settings area.** For example, if your app lets people adjust things like showing or hiding parts of the interface, reordering a collection of items, or filtering a list, make these options available in the screens they affect, where they’re discoverable and convenient. Putting this type of option in a separate settings area disconnects it from its context, requiring people to suspend their task to make adjustments, and often hiding the results until people resume the task.
> 가능한 설정 영역으로 이동하지 않고 작업별 옵션을 수정할 수 있습니다. 예를 들어, 앱에서 인터페이스의 일부를 표시하거나 숨기거나, 항목 모음을 다시 정렬하거나, 목록을 필터링하는 등의 작업을 조정할 수 있는 경우, 이러한 옵션을 검색 가능하고 편리한 화면에서 사용할 수 있도록 합니다. 이러한 유형의 옵션을 별도의 설정 영역에 두면 컨텍스트와 연결이 끊겨 사용자가 작업을 일시 중지하여 조정해야 하며, 작업을 다시 시작할 때까지 결과를 숨기는 경우가 많습니다.
>




**When necessary, put app-level options in a separate settings area.** People don’t tend to visit an app’s settings area very often, so it’s important to include only rarely-changed options that affect the experience as a whole, such as overall interface style or alternative app icons.
> 필요한 경우 별도의 설정 영역에 앱 수준 옵션을 배치합니다. 사람들은 앱의 설정 영역을 자주 방문하지 않는 경향이 있으므로 전체적인 인터페이스 스타일이나 대체 앱 아이콘과 같이 전체적으로 환경에 영향을 미치는 거의 변경되지 않은 옵션만 포함하는 것이 중요하다.
>




**Minimize the number of settings you offer.** Although people appreciate having control over an app, they also appreciate being able to benefit from the experience without first doing a lot of setup. Too many settings can make an app feel less approachable, while also making it hard to find a particular setting.
> 제공하는 설정 수를 최소화합니다. 비록 사람들이 앱을 제어할 수 있다는 것은 감사하지만, 그들은 또한 많은 설정을 하지 않고도 경험으로부터 이익을 얻을 수 있다는 것에 감사한다. 설정이 너무 많으면 특정 설정을 찾기 어려울 뿐만 아니라 앱의 접근성이 떨어질 수 있습니다.
>




**Respect people’s systemwide settings and avoid including redundant versions of them in your app-specific settings area.** People expect to use the system-provided settings apps to manage global options like accessibility accommodations, scrolling behavior, and authentication methods, and they expect all apps to adhere to their choices. Offering app-specific settings that include custom versions of global options is inconsistent and confusing in at least two ways: First, it implies that systemwide settings may not apply to the current app and second, that changing one of the app’s custom settings can affect other apps too.
> 사용자의 시스템 전체 설정을 존중하고 앱별 설정 영역에 중복 버전을 포함하지 않도록 합니다. 사람들은 시스템이 제공하는 설정 앱을 사용하여 접근성 숙소, 스크롤 동작 및 인증 방법과 같은 글로벌 옵션을 관리할 것으로 기대하며, 모든 앱이 자신의 선택을 고수할 것으로 기대한다. 글로벌 옵션의 사용자 지정 버전을 포함하는 앱별 설정을 제공하는 것은 적어도 두 가지 면에서 일관성이 없고 혼란스럽다. 첫째, 시스템 전체 설정이 현재 앱에 적용되지 않을 수 있음을 의미하며, 둘째, 앱의 사용자 지정 설정 중 하나를 변경하면 다른 앱에도 영향을 미칠 수 있습니다.
>




**Avoid using in-app settings to ask for setup information you can get in other ways.** For example, instead of asking someone to enter a zip code so you can present local options, ask permission to use their current location. For guidance, see [Accessing private data](../patterns/accessing-private-data).
> 앱 내 설정을 사용하여 다른 방법으로 얻을 수 있는 설정 정보를 묻지 않도록 합니다. 예를 들어 로컬 옵션을 표시할 수 있도록 다른 사용자에게 우편 번호를 입력하도록 요청하는 대신 현재 위치를 사용할 수 있는 권한을 요청합니다. 자세한 내용은 개인 데이터 액세스를 참조하십시오.
>




**Add only the most rarely changed options to the system-provided settings apps.** On each platform, the system includes an app that lets people adjust things like the overall appearance of the system, network connections, account details, accessibility requirements, and language and region settings. Although both the Settings app (in iOS, iPadOS, and tvOS) and the System Settings app (in macOS) can also contain app-specific settings, people must switch away from their current context to adjust those settings. If you must offer app-specific settings in the system settings apps, consider providing a button that opens them directly from your app.
> 시스템에서 제공하는 설정 앱에 가장 드물게 변경된 옵션만 추가합니다. 각 플랫폼에는 시스템의 전체적인 모양, 네트워크 연결, 계정 세부 정보, 접근성 요구사항, 언어 및 지역 설정 등을 조정할 수 있는 앱이 포함되어 있다. 설정 앱(iOS, iPadOS 및 tvOS)과 시스템 설정 앱(macOS)도 앱별 설정을 포함할 수 있지만, 이러한 설정을 조정하려면 현재 컨텍스트에서 전환해야 합니다. 시스템 설정 앱에서 앱별 설정을 제공해야 하는 경우 앱에서 직접 여는 버튼을 제공하는 것을 고려해 보십시오.
>




**Make your in-app settings easy to find, but not too prominent.** For example, consider making settings available within a profile or account view. In a watchOS app, you could make a very small number of essential options available at the bottom of the main view.
> 앱 내 설정을 쉽게 찾을 수 있지만 너무 눈에 띄지 않도록 하십시오. 예를 들어 프로파일 또는 계정 보기 내에서 설정을 사용할 수 있도록 설정하는 것을 고려해 보십시오. 시계로OS 앱에서 기본 보기 하단에 매우 적은 수의 필수 옵션을 사용할 수 있습니다.
>




**In macOS and iPadOS apps, make settings available in ways people expect.** For example, people appreciate being able to use the standard Command-Comma (,) keyboard shortcut to open app-level settings. In an app that runs on a Mac, include an app-level settings item in the [App menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#app-menu) and, if you provide document-level options, add this item to the [File menu](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/the-menu-bar#file-menu). Avoid adding settings buttons to a macOS app’s toolbar, because doing so decreases the space available for essential commands that people use frequently.
> macOS 및 iPadOS 앱에서 사람들이 기대하는 방식으로 설정을 사용할 수 있도록 합니다. 예를 들어, 표준 Command-Comma(,) 바로 가기 키를 사용하여 앱 수준 설정을 열 수 있다는 점을 높이 평가합니다. Mac에서 실행되는 앱에서 앱 메뉴에 앱 수준 설정 항목을 포함하고 문서 수준 옵션을 제공하는 경우 이 항목을 파일 메뉴에 추가합니다. 설정 단추를 macOS 앱의 도구 모음에 추가하지 마십시오. 이렇게 하면 사람들이 자주 사용하는 필수 명령에 사용할 수 있는 공간이 줄어들기 때문입니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or tvOS.*
> iOS, iPadOS 또는 tvOS에 대한 추가 고려 사항 없음.
>




# **macOS**

An app-specific window opens when people choose the Settings item in the App menu. Typically, an app-specific settings window contains a toolbar that includes buttons for switching between views — called *panes* — that each contain a group of related settings.
> 앱 메뉴에서 설정 항목을 선택하면 앱별 창이 열립니다. 일반적으로 앱별 설정 창에는 보기 간 전환(창이라고 함)을 위한 단추가 포함된 도구 모음이 있으며 각 도구 모음에는 관련 설정 그룹이 포함되어 있습니다.
>




**Disable a settings window’s minimize and maximize buttons.** It’s quick to open a settings window using the standard Command–Comma (,) keyboard shortcut, so there’s no need to keep the window in the Dock, and because a settings window accommodates the size of the current pane, people don’t need to expand the window to see more.
> 설정 창의 최소화 및 최대화 버튼을 비활성화합니다. 표준 Command-Comma(,) 바로 가기 키를 사용하여 설정 창을 빨리 열 수 있으므로 창을 도크에 보관할 필요가 없으며 설정 창은 현재 창의 크기를 수용하므로 사용자가 창을 확장하여 더 많이 볼 필요가 없습니다.
>




**Provide a noncustomizable toolbar that remains visible and always indicates the active toolbar button.** A settings window’s toolbar identifies the areas people can customize and enables navigation among those areas. People rely on a stable settings interface to help them find what they need.
> 사용자 정의할 수 없는 도구 모음을 제공하고 항상 활성 도구 모음 단추를 표시합니다. 설정 창의 도구 모음은 사용자가 사용자 정의할 수 있는 영역을 식별하고 해당 영역 사이를 탐색할 수 있도록 합니다. 사람들은 그들이 필요한 것을 찾는 것을 돕기 위해 안정적인 설정 인터페이스에 의존한다.
>




**Update the window's title to reflect the currently visible pane.** If your settings window doesn’t have multiple panes, use the title *App Name* Settings.
> 창 제목을 업데이트하여 현재 표시된 창을 반영합니다. 설정 창에 여러 개의 창이 없으면 앱 이름 설정 제목을 사용하십시오.
>




**Restore the most recently viewed pane.** People often adjust related settings more than once, so it can be convenient when a settings window opens to the last pane people used.
> 가장 최근에 본 창을 복원합니다. 사람들은 종종 관련 설정을 두 번 이상 조정하기 때문에 사람들이 마지막으로 사용한 창으로 설정 창이 열릴 때 편리할 수 있다.
>




# **watchOS**

Avoid supplying app-specific settings to include in the watchOS Settings app.
> 워치에 포함할 앱별 설정을 제공하지 마십시오.OS 설정 앱.
>



