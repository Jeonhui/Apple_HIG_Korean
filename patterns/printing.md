# **[patterns] printing**

# An iOS, iPadOS, or macOS app can integrate system-provided print functionality when it makes sense, presenting custom printer- and document-specific options if necessary.
> iOS, iPadOS 또는 macOS 앱은 시스템이 제공하는 인쇄 기능을 통합하여 필요한 경우 사용자 지정 프린터 및 문서별 옵션을 제공할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-printing-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-printing-intro-dark_2x.png)

# **Best practices**

**Make printing discoverable.** Help people find your print action by placing it in standard system locations. For example, include a Print item in your macOS app’s File menu; in your iOS or iPadOS app, add a toolbar or navigation bar button that opens an [action sheet](../components/presentation/action-sheets/). If your macOS app has a toolbar, you might want to put a Print button there, too, but consider making it an optional button that people can add when they customize the toolbar.
> 인쇄를 검색할 수 있도록 합니다. 인쇄 작업을 표준 시스템 위치에 배치하여 다른 사용자가 찾을 수 있도록 지원합니다. 예를 들어 macOS 앱의 파일 메뉴에 인쇄 항목을 포함시키고 iOS 또는 iPadOS 앱에서 작업 시트를 여는 도구 모음 또는 탐색 모음 단추를 추가합니다. macOS 앱에 도구 모음이 있는 경우 인쇄 단추도 함께 넣을 수 있지만 도구 모음을 사용자 지정할 때 추가할 수 있는 옵션 단추로 만드는 것을 고려해 보십시오.
>




**Enable printing only when printing is possible.** If there’s nothing onscreen to print, or no printers are available, disable the Print item in a macOS app’s File menu and remove the Print action from the Action sheet in an iOS or iPadOS app. If you implement a custom print button, disable or hide it when printing isn’t possible.
> 인쇄가 가능한 경우에만 인쇄를 활성화합니다. 화면에 인쇄할 것이 없거나 사용할 수 있는 프린터가 없는 경우 MacOS 앱의 파일 메뉴에서 인쇄 항목을 사용하지 않도록 설정하고 iOS 또는 iPadOS 앱의 작업 시트에서 인쇄 작업을 제거합니다. 사용자 지정 인쇄 단추를 구현하는 경우 인쇄할 수 없는 경우 사용 불가능으로 설정하거나 숨깁니다.
>




**Enable relevant printing options.** If it makes sense to offer options like selecting a page range, requesting multiple copies, or printing on both sides — and the printer supports the options — use the system-provided view to enable them.
> 관련 인쇄 옵션을 활성화합니다. 페이지 범위 선택, 여러 복사본 요청 또는 양면 인쇄와 같은 옵션을 제공하는 것이 타당하고 프린터가 옵션을 지원하는 경우 시스템에서 제공한 보기를 사용하여 옵션을 활성화합니다.
>




# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in tvOS or watchOS.*
> iOS 또는 iPad OS에 대한 추가 고려 사항 없음. tvOS 또는 시계에서 지원되지 않음OS.
>




# **macOS**

**If your macOS app enables app-specific print options that the system doesn’t offer, consider creating a custom category for the print panel.** By default, the print panel offers several categories of settings, such as Layout, Paper Handling, and Media & Quality. Give your custom category a unique name, such as your app name, and include options that help people have a great print experience in your app. For example, Keynote offers presentation-specific options, like the ability to print presenter notes, slide backgrounds, and skipped slides.
> macOS 앱에서 시스템에서 제공하지 않는 앱별 인쇄 옵션을 사용할 수 있는 경우 인쇄 패널에 대한 사용자 지정 범주를 만드는 것을 고려해 보십시오. 기본적으로 인쇄 패널은 레이아웃, 용지 처리, 미디어 및 품질과 같은 몇 가지 범주의 설정을 제공합니다. 사용자 정의 범주에 앱 이름과 같은 고유한 이름을 지정하고 다른 사용자가 앱에서 멋진 인쇄 경험을 할 수 있도록 지원하는 옵션을 포함합니다. 예를 들어, Keynote는 발표자 노트 인쇄, 배경 슬라이드 및 건너뛴 슬라이드와 같은 프레젠테이션 관련 옵션을 제공합니다.
>




**If your app enables document-specific page settings, consider presenting a page setup dialog.** A *page setup dialog* includes rarely changed settings for page size, orientation, and scaling that apply to printing a particular document. If this makes sense in your app, avoid implementing features the system already provides. For example, you don’t need to include options like changing the page orientation or printing in reverse order because the system implements these options.
> 앱에서 문서별 페이지 설정을 사용할 수 있는 경우 페이지 설정 대화 상자를 표시하는 것을 고려해 보십시오. 페이지 설정 대화상자에는 특정 문서 인쇄에 적용되는 페이지 크기, 방향 및 축척에 대한 설정이 거의 변경되지 않습니다. 이것이 당신의 앱에서 타당하다면, 시스템이 이미 제공하는 기능을 구현하는 것을 피하세요. 예를 들어, 시스템은 페이지 방향을 변경하거나 역순으로 인쇄하는 등의 옵션을 포함할 필요가 없습니다.
>




**Make sure interdependencies between options are clear.** For example, if double-sided printing is enabled, an option to print on transparencies becomes unavailable.
> 옵션 간의 상호 의존성이 명확해야 합니다. 예를 들어 양면 인쇄가 활성화된 경우 투명 필름에 인쇄하는 옵션을 사용할 수 없습니다.
>




