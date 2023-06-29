# **[components-presentation] windows**

## A window contains the views and components that present the user interface of your app or game.
> 창에는 앱 또는 게임의 사용자 인터페이스를 표시하는 보기와 구성 요소가 포함되어 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/window-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/window-intro-dark_2x.png)

Depending on the platform, device, and context, a window (or *scene*) can be undetectable. For example, in platforms where the default experience is full screen, like iOS, tvOS, and watchOS, people view and interact with the content inside a window — they don't view or interact with the window itself. In these cases, you don't need to design the appearance of the windows or scenes in your app or game. For developer guidance, see [Scene](https://developer.apple.com/documentation/swiftui/scene) and [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow).
> 플랫폼, 장치 및 컨텍스트에 따라 창(또는 장면)이 감지되지 않을 수 있습니다. 예를 들어 iOS, TVOS 및 watchOS와 같이 기본적으로 전체 화면을 사용하는 플랫폼에서는 창 자체를 보거나 창과 상호 작용하지 않고 창 내부의 콘텐츠를 보고 상호 작용합니다. 이 경우 앱이나 게임에서 창이나 장면의 모양을 설계할 필요가 없습니다. 개발자 지침은 장면 및 UI 창을 참조하십시오.
>




In contrast, iPadOS supports multitasking and multiple windows, so people can be aware of an app’s window as a visually distinct object. For example, people can view two or three apps onscreen at the same time or open multiple windows in the same app. To create a great iPadOS experience, you need to ensure that your windows and scenes look and behave the way people expect. For guidance, see [Multitasking](../patterns/multitasking); for developer guidance, see [Scenes](https://developer.apple.com/documentation/uikit/app_and_environment/scenes).
> 대조적으로, 아이패드OS는 멀티태스킹과 여러 창을 지원하므로 사람들은 앱의 창을 시각적으로 구별되는 객체로 인식할 수 있다. 예를 들어, 사람들은 화면에서 두 개 또는 세 개의 앱을 동시에 보거나 같은 앱에서 여러 개의 창을 열 수 있다. 훌륭한 iPad를 만들려면OS 경험을 바탕으로 창과 장면이 사람들이 기대하는 방식으로 표시되고 작동하는지 확인해야 합니다. 자세한 내용은 멀티태스킹을 참조하고, 개발자 지침은 장면을 참조하십시오.
>




In macOS, people are accustomed to interacting with app windows as distinct objects. Mac users typically run several apps at the same time, often viewing windows from multiple apps on one desktop and switching frequently between different windows — moving, resizing, minimizing, and revealing the windows to suit their work style. Even when people choose full-screen mode, which usually hides the window frame, the built-in, full-screen transition and the ability to reveal the toolbar remind them of the existence of the window.
> macOS에서 사람들은 앱 창과 별개의 객체로 상호작용하는 것에 익숙하다. Mac 사용자는 일반적으로 여러 개의 앱을 동시에 실행하며, 종종 한 데스크톱의 여러 앱에서 창을 보고 서로 다른 창을 자주 전환하여 작업 스타일에 맞게 창을 이동, 크기 조정, 최소화 및 표시합니다. 사람들이 보통 창틀을 숨기는 풀스크린 모드를 선택할 때도 내장된 풀스크린 전환과 툴바를 드러내는 기능은 창의 존재를 떠올리게 한다.
>




**IMPORTANT**The guidance below applies to windows in macOS. For guidance on other types of window-like views in all platforms, see [Alerts](../components/presentation/alerts), [Panels](../components/presentation/panels),  [Popovers](../components/presentation/popovers), and [Sheets](../components/presentation/sheets).
> 중요 아래 지침은 MacOS의 창에 적용됩니다. 모든 플랫폼의 다른 유형의 창 모양 보기에 대한 지침은 경고, 패널, 팝업 및 시트를 참조하십시오.
>




# **macOS window anatomy**

A macOS window consists of a frame and a body area. People can move a window by dragging the frame and can often resize the window by dragging its edges.
> MacOS 창은 프레임과 본체 영역으로 구성됩니다. 사람들은 프레임을 끌어서 창을 이동할 수 있으며 종종 가장자리를 끌어서 창 크기를 조정할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-anatomy_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-anatomy_2x.png)

The *frame* is the portion of a window that surrounds body content. A window frame can include a title bar, [toolbar](../components/menus-and-actions/toolbars), [tabs](../components/layout-and-organization/tab-views), and (in rare cases) a bottom bar.
> 프레임은 본문 내용을 둘러싸는 창의 부분입니다. 창 프레임에는 제목 표시줄, 도구 모음, 탭 및 드물게 하단 표시줄이 포함될 수 있습니다.
>




The window *body* displays the main content of the window. This content can fill the entire body area — such as a website in a Safari window or an image in Preview — or the content can display in multiple subviews, such as in a [split view](../components/layout-and-organization/split-views) interface. Content that extends beyond the bounds of views in the body area is scrollable.
> 창 본문에는 창의 주요 내용이 표시됩니다. 이 콘텐츠는 Safari 창의 웹 사이트나 미리 보기의 이미지와 같은 전체 본문 영역을 채우거나 분할 보기 인터페이스와 같은 여러 하위 보기에 콘텐츠를 표시할 수 있습니다. 본문 영역의 보기 범위를 벗어나는 내용은 스크롤할 수 있습니다.
>




# **macOS window states**

A macOS window can have one of three states:
> MacOS 창은 다음 세 가지 상태 중 하나를 가질 수 있습니다.
>




- **Main.** The frontmost window that people focus on is an app’s main window. There can be only one main window per app.
- >  메인. 사람들이 가장 앞에 집중하는 창은 앱의 메인 창이다. 앱당 기본 창은 하나만 있을 수 있습니다.

- **Key.** Also called the active window, the key window accepts people’s input. There can be only one key window onscreen at a time. Although the front app’s main window is usually the key window, another window — such as a panel floating above the main window — might be key instead. People typically click a window to make it key; when people click an app’s Dock icon to bring all of that app’s windows forward, only the most recently accessed window becomes key.
- >  키. 활성 창이라고도 불리는 키 창은 사람들의 입력을 받아들입니다. 화면에는 한 번에 하나의 키 창만 표시될 수 있습니다. 전면 앱의 주 창이 일반적으로 키 창이지만, 주 창 위에 떠 있는 패널과 같은 다른 창이 대신 키가 될 수 있습니다. 사용자는 일반적으로 창을 클릭하여 키를 만듭니다. 사용자가 앱의 도킹 아이콘을 클릭하여 해당 앱의 모든 창을 앞으로 가져오면 가장 최근에 액세스한 창만 키가 됩니다.

- **Inactive.** A window that’s not in the foreground is an inactive window.
- >  비활성입니다. 전면에 없는 창은 비활성 창입니다.


The system gives main, key, and inactive windows different appearances to help people visually identify them. For example, the key window uses color in the title bar options for closing, minimizing, and zooming; inactive windows and main windows that aren’t key use gray in these options. Also, inactive windows don’t use [vibrancy](../foundations/materials) (an effect that can pull color into a window from the content underneath it), which makes them appear subdued and seem visually farther away than the main and key windows.
> 이 시스템은 메인, 키 및 비활성 창을 시각적으로 식별할 수 있도록 다양한 모양을 제공합니다. 예를 들어, 키 창은 제목 표시줄 옵션의 색상을 사용하여 닫기, 최소화 및 확대/축소합니다. 비활성 창과 키가 아닌 기본 창은 회색을 사용합니다. 또한 비활성 창은 진동(아래 내용에서 창으로 색을 끌어들일 수 있는 효과)을 사용하지 않으므로 메인 창과 키 창보다 시각적으로 더 멀리 보이는 것처럼 보입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-states_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/windows/images/window-states_2x.png)

**NOTE**Some windows — typically, panels like Colors or Fonts — become the key window only when people click the window's title bar or a component that requires keyboard input, such as a text field.
> 참고일반적으로 색 또는 글꼴과 같은 패널은 사용자가 창 제목 표시줄이나 텍스트 필드와 같이 키보드 입력이 필요한 구성요소를 클릭할 때만 키 창이 됩니다.
>




# **Best practices**

**Make sure your custom windows use the system-defined appearances.**People rely on the visual differences in various onscreen windows to help them identify the foreground window and know which window will accept their input. When you use system-provided components, a window’s background and button appearances update automatically when the window changes state; if you use custom implementations, you need to do this work yourself.
> 사용자 지정 창에서 시스템 정의 모양을 사용하는지 확인합니다.사람들은 전경 창을 식별하고 어떤 창이 입력을 받아들일지 알기 위해 다양한 화면 창의 시각적 차이에 의존한다. 시스템에서 제공하는 구성 요소를 사용하면 창 상태가 변경될 때 창 배경 및 단추 모양이 자동으로 업데이트됩니다. 사용자 지정 구현을 사용하는 경우 이 작업을 직접 수행해야 합니다.
>




**Display a title unless the window’s content provides enough context to make one unnecessary.** For document windows, the title is the name of the document or *Untitled* (for new documents). For app windows, the title is the name of the app.
> 창의 내용이 불필요한 컨텍스트를 제공하지 않는 한 제목을 표시합니다. 문서 창의 경우 제목은 문서의 이름이거나 제목 없음(새 문서의 경우)입니다. 앱 창의 경우 제목은 앱의 이름입니다.
>




**If you need to use a filename as a title, make it easy to understand.** For example, use the file’s *display name,* which reflects people’s preference for showing or hiding a file extension and may be localized.
> 파일 이름을 제목으로 사용해야 하는 경우 파일 이름을 쉽게 이해할 수 있습니다. 예를 들어, 파일 확장명을 표시하거나 숨기려는 사용자의 선호도를 반영하고 지역화될 수 있습니다.
>




**Avoid including a file system path in the title bar.** Paths are generally too long to fit in the title bar without clipping, and they’re difficult for people to understand at a glance. If you need to show the complete path of a file or folder, do so in another way, like in an inspector pane.
> 파일 시스템 경로는 일반적으로 제목 표시줄에 너무 길어서 클리핑 없이는 들어갈 수 없으며 사용자가 한 눈에 보기 어렵습니다. 파일 또는 폴더의 전체 경로를 표시해야 하는 경우 검사기 창에서와 같은 다른 방법으로 표시합니다.
>




**Use numeric suffixes to differentiate duplicate titles.** The first instance of a title doesn't need a numeric suffix. When other windows have the same title, append numeric suffixes, starting with *2*. For example, *Untitled*, *Untitled 2*, *Untitled 3*.
> 중복 제목을 구분하려면 숫자 접미사를 사용하십시오. 제목의 첫 번째 인스턴스에는 숫자 접미사가 필요하지 않습니다. 다른 창에 동일한 제목이 있으면 2로 시작하는 숫자 접미사를 추가합니다. 예를 들어, 제목 없음, 제목 없음 2, 제목 없음 3입니다.
>




**Make sure people can still interact with your window if you hide the title bar.** Provide alternative ways — like menus — to close and minimize the window. Make sure people can still drag the frame to move the window. If the window has a toolbar and no title bar, make sure there’s enough space in the toolbar to drag the window without activating toolbar items.
> 제목 표시줄을 숨기더라도 다른 사용자가 창과 상호 작용할 수 있는지 확인하십시오. 메뉴와 같은 다른 방법으로 창을 닫고 최소화할 수 있습니다. 창을 이동하기 위해 사람들이 프레임을 끌 수 있는지 확인합니다. 창에 도구 모음이 있고 제목 표시줄이 없는 경우 도구 모음 항목을 활성화하지 않고 창을 끌 수 있는 공간이 충분한지 확인합니다.
>




**In general, use a dot to mark a modified document as unsaved only when it can't be autosaved.** If a document can be autosaved, you don't want to display a dot in the window's close button or next to the document’s name in the Window menu because doing so signals that people need to take action to save their changes. It’s fine to append a suffix like *Edited* to the document's title in the title bar, but you need to remove this suffix when it autosaves or if people manually perform a save.
> 자동으로 저장할 수 없는 경우에만 수정된 문서를 저장하지 않은 것으로 표시하려면 일반적으로 점을 사용합니다. 문서를 자동으로 저장할 수 있는 경우 창 메뉴에서 창 닫기 단추나 문서 이름 옆에 점을 표시하면 변경 내용을 저장하기 위해 작업을 수행해야 한다는 신호를 표시하기 때문입니다. 제목 표시줄의 문서 제목에 편집된 것과 같은 접미사를 추가하는 것은 좋지만 자동으로 저장하거나 사용자가 수동으로 저장을 수행할 경우 이 접미사를 제거해야 합니다.
>




**Use a bottom bar to display a small amount of information directly related to a window’s contents or to a selected item within it.** For example, Finder uses a bottom bar (called the Status Bar) to display the total number of items in a window, the number of selected items, and how much space is available on the disk. A bottom bar is small, so if you have more information to display, consider using an inspector, which typically presents information on the trailing side of a split view.
> 아래쪽 막대를 사용하여 창의 내용 또는 창의 선택한 항목과 직접 관련된 소량의 정보를 표시합니다. 예를 들어, Finder는 아래쪽 막대(상태 표시줄)를 사용하여 창에 있는 총 항목 수, 선택한 항목 수 및 디스크에서 사용 가능한 공간을 표시합니다. 아래쪽 막대는 작으므로 표시할 정보가 더 있으면 일반적으로 분할 뷰의 뒤쪽에 정보를 표시하는 검사기를 사용하는 것이 좋습니다.
>




**Avoid putting critical information or actions in a bottom bar.** People often relocate a window in a way that hides its bottom edge.
> 중요한 정보나 작업을 하단 표시줄에 넣지 마십시오. 사람들은 종종 하단 모서리를 숨기는 방식으로 창을 재배치합니다.
>




# **Platform considerations**

*No additional considerations for iOS, macOS, tvOS, or watchOS.*
> iOS, macOS, tvOS 또는 시계에 대한 추가 고려 사항 없음운영 체제
>




# **iPadOS**

To support multitasking and multiwindow workflows on iPad, you need to ensure that your windows adapt to different sizes and that you match each window's presentation style to its content. For guidance, see [Multitasking on iPad](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking#multitasking-on-ipad).
> iPad에서 멀티태스킹 및 멀티윈도우 워크플로우를 지원하려면 창이 다양한 크기에 맞게 조정되고 각 창의 프레젠테이션 스타일이 내용에 맞게 조정되도록 해야 합니다. 자세한 내용은 iPad의 멀티태스킹을 참조하십시오.
>



