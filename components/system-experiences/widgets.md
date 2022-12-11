# **[components-status] widgets**

## A widget elevates a small amount of timely, personally relevant information from your app or game, displaying it where people can see it at a glance.
> 위젯은 앱이나 게임에서 개인적으로 관련된 소량의 정보를 적시에 끌어올려 사람들이 한 눈에 볼 수 있는 위치에 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/widgets-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/widgets-intro-dark_2x.png)

Widgets display app content without requiring people to open your app. Useful and delightful, widgets can also help people make their devices more personal. For developer guidance, see [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension).
> 위젯은 사용자가 앱을 열지 않아도 앱 콘텐츠를 표시합니다. 유용하고 즐거운 위젯은 또한 사람들이 기기를 더 개인적으로 만들 수 있도록 도와줍니다. 개발자 지침은 위젯 확장자 만들기를 참조하십시오.
>




In iOS and iPadOS, widgets appear on the Home Screen or in Today View; in macOS, Notification Center displays widgets. Widgets can be small, medium, large, and — in iPadOS only — extra large.
> iOS 및 iPadOS에서는 위젯이 홈 화면 또는 오늘 보기에 표시되고, macOS에서는 Notification Center가 위젯을 표시합니다. 위젯은 소형, 중형, 대형 및 iPad에서 사용할 수 있습니다.OS만 해당 — 특대형.
>




iOS 16 introduces widgets on the Lock Screen, which let people place rich, glanceable content on their iPhone Lock Screen in a way that’s similar to placing a complication on their Apple Watch face. Lock Screen widgets are also similar to complications in both design and implementation. For guidance, see [Platform considerations](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets#platform-considerations) below.
> iOS 16은 잠금 화면에 위젯을 도입하여 사람들이 아이폰 잠금 화면에 풍부하고 눈에 띄는 콘텐츠를 애플 워치의 얼굴에 복잡하게 배치하는 것과 유사한 방식으로 배치할 수 있도록 한다. 잠금 화면 위젯은 또한 설계와 구현 모두에서 복잡성과 유사합니다. 자세한 내용은 아래 플랫폼 고려사항을 참조하십시오.
>




The widget gallery helps people find the widgets they want in the sizes that work for them. The gallery’s editing mode lets people make changes to editable widgets, such as changing the location in a Weather widget or selecting a topic in a News widget. The widget gallery is available in Today View and Home Screen editing mode in iOS and iPadOS. It’s also available in Lock Screen editing mode in iOS and in Notification Center editing mode in macOS.
> 위젯 갤러리는 사용자가 원하는 크기의 위젯을 찾을 수 있도록 도와줍니다. 갤러리의 편집 모드를 사용하면 날씨 위젯에서 위치를 변경하거나 뉴스 위젯에서 주제를 선택하는 등 편집 가능한 위젯을 변경할 수 있습니다. 위젯 갤러리는 iOS 및 iPadOS에서 오늘 보기 및 홈 화면 편집 모드로 사용할 수 있습니다. iOS에서는 잠금 화면 편집 모드, MacOS에서는 알림 센터 편집 모드에서도 사용할 수 있습니다.
>




In iOS and iPadOS, the widget gallery also supports widget stacks, including a Smart Stack. A stack contains up to 10 same-size widgets; people view one widget at a time by scrolling through the stack. A Smart Stack automatically rotates through the stack of widgets, displaying the widget most likely to be relevant in the current context. Smart Stacks aren't available on the Lock Screen on iPhone and iPad.
> iOS와 아이패드 OS에서 위젯 갤러리는 스마트 스택을 포함한 위젯 스택도 지원합니다. 스택은 최대 10개의 동일한 크기의 위젯을 포함하며, 사용자는 스택을 스크롤하여 한 번에 하나의 위젯을 봅니다. 스마트 스택은 위젯 스택을 통해 자동으로 회전하여 현재 컨텍스트와 가장 관련성이 높은 위젯을 표시합니다. 스마트 스택은 iPhone과 iPad의 잠금 화면에서 사용할 수 없습니다.
>




Siri can add a suggested widget to the Smart Stack when it’s likely that people are interested in it. A suggested widget doesn’t stay in the Smart Stack unless people choose to keep it. For developer guidance, see [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks).
> Siri는 사람들이 스마트 스택에 관심을 가질 가능성이 있을 때 제안된 위젯을 추가할 수 있습니다. 제안된 위젯은 사용자가 유지하도록 선택하지 않는 한 스마트 스택에 유지되지 않습니다. 개발자 지침은 스마트 스택에서 위젯 가시성 향상을 참조하십시오.
>




# **Best practices**

The first step in the design process is to choose a single idea for your widget. Throughout the process, use that idea to keep the widget’s content focused and relevant.
> 설계 프로세스의 첫 번째 단계는 위젯에 대한 단일 아이디어를 선택하는 것입니다. 프로세스 전반에 걸쳐 이 아이디어를 사용하여 위젯의 콘텐츠에 초점을 맞추고 관련성을 유지합니다.
>




**Look for a simple idea that’s clearly related to your app’s main purpose.** For example, the widget for Weather shows current high and low temperatures plus the current weather conditions. This is the information most people who use the Weather app are primarily interested in. Alternatively, another weather app might offer people the ability to see other types of weather data such as pressure, humidity, or wind speed.
> 예를 들어 날씨 위젯에서는 현재 고온 및 저온과 현재 날씨 상태를 보여 줍니다. 이것은 날씨 앱을 사용하는 대부분의 사람들이 주로 관심을 갖는 정보입니다. 또는 다른 날씨 앱은 사람들에게 압력, 습도 또는 풍속과 같은 다른 유형의 날씨 데이터를 볼 수 있는 능력을 제공할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/focused-widget_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/focused-widget_2x.png)

**In each size, display only the information that’s directly related to the widget’s main purpose.** In larger widgets, you can display more data — or more detailed visualizations of the data — but it’s crucial to stay focused on the widget’s purpose. For example, all Calendar widgets display a person’s upcoming events. In each size from small to extra large, the widget maintains its focus on events while expanding the range of information as the size increases.
> 각 크기에는 위젯의 주요 목적과 직접 관련된 정보만 표시합니다. 큰 위젯에서는 더 많은 데이터 또는 데이터의 더 자세한 시각화를 표시할 수 있지만 위젯의 목적에 집중하는 것이 중요합니다. 예를 들어, 모든 일정관리 위젯은 사용자의 예정된 이벤트를 표시합니다. 작은 것부터 큰 것까지 각각의 크기에서 위젯은 이벤트에 대한 초점을 유지하면서 크기가 증가함에 따라 정보의 범위를 확장합니다.
>




• [Small](../components/system-experiences/widgets#)
• [Medium](../components/system-experiences/widgets#)
• [Large](../components/system-experiences/widgets#)
• [Extra Large (iPad only)](../components/system-experiences/widgets#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/calendar-small_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/calendar-small_2x.png)


**Avoid creating a widget that only launches your app.** People appreciate widgets because they provide instant access to meaningful content. A widget that behaves like an app icon offers no additional value, which means people are likely to remove it from their screens.
> 앱만 시작하는 위젯을 만들지 마십시오. 위젯은 의미 있는 콘텐츠에 즉시 액세스할 수 있기 때문에 사람들이 위젯을 높이 평가합니다. 앱 아이콘처럼 행동하는 위젯은 추가적인 가치를 제공하지 않으며, 이는 사람들이 화면에서 위젯을 제거할 가능성이 높다는 것을 의미합니다.
>




**Offer your widget in multiple sizes when doing so adds value.** In general, avoid simply expanding a smaller widget’s content to fill a larger area. It’s more important to create one widget in the size that works best for the content you want to display than it is to provide the widget in all sizes.
> 위젯을 여러 크기로 제공하여 가치를 높입니다. 일반적으로 작은 위젯의 내용을 단순히 확장하여 더 큰 영역을 채우지 마십시오. 모든 크기의 위젯을 제공하는 것보다 표시할 내용에 가장 적합한 크기의 위젯을 하나 만드는 것이 더 중요합니다.
>




**Prefer dynamic information that changes throughout the day.** If a widget’s content never appears to change, people may not keep it in a prominent position. Although widgets don’t update from minute to minute, it’s important to find ways to keep their content fresh to invite frequent viewing.
> 하루 종일 변화하는 동적 정보를 선호합니다. 위젯의 내용이 절대 변하지 않는 것처럼 보일 경우 사람들이 눈에 띄는 위치에 유지하지 못할 수 있습니다. 위젯이 시시각각 업데이트되지는 않지만 자주 볼 수 있도록 내용을 새로 유지하는 방법을 찾는 것이 중요합니다.
>




**Look for opportunities to surprise and delight.** For example, you might design a unique visual treatment for your calendar widget to display on meaningful occasions, like birthdays or holidays.
> 예를 들어, 생일이나 공휴일과 같은 의미 있는 경우에 달력 위젯이 표시할 수 있는 고유한 시각적 처리를 설계할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/surprise-and-delight_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/surprise-and-delight_2x.png)

# **Updating widget content**

To remain relevant and useful, widgets periodically refresh their information. Widgets don’t support continuous, real-time updates, and the system may adjust the limits for updates depending on various factors.
> 관련성과 유용성을 유지하기 위해 위젯은 주기적으로 정보를 새로 고칩니다. 위젯은 지속적인 실시간 업데이트를 지원하지 않으며, 시스템은 다양한 요인에 따라 업데이트 제한을 조정할 수 있습니다.
>




**Keep your widget up to date.** Finding the appropriate update frequency for your widget depends on knowing how often the data changes and estimating how often people need to see new data. For example, a widget that helps people track tides at a beach could provide useful information on an hourly basis, even though tide conditions change constantly. If people are likely to check your widget more frequently than you can update it, consider displaying text that describes when the data was last updated. For developer guidance, see [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date).
> 위젯을 최신 상태로 유지합니다. 위젯에 적합한 업데이트 빈도를 찾는 방법은 데이터가 변경되는 빈도를 알고 사용자가 새 데이터를 보는 빈도를 추정하는 방법에 따라 달라집니다. 예를 들어, 사람들이 해변에서 조수를 추적하는 것을 돕는 위젯은 조수의 조건이 끊임없이 변화하더라도 시간 단위로 유용한 정보를 제공할 수 있다. 사용자가 업데이트할 수 있는 것보다 더 자주 위젯을 확인하는 경우 데이터가 마지막으로 업데이트된 시간을 설명하는 텍스트를 표시하는 것이 좋습니다. 개발자 지침은 위젯을 최신 상태로 유지를 참조하십시오.
>




**Let the system update dates and times in your widget.** Widget update frequency is limited, and you can preserve some of your update opportunities by letting the system refresh date and time information.
> 위젯의 날짜 및 시간을 시스템에서 업데이트하도록 합니다. 위젯 업데이트 빈도는 제한적이며, 시스템에서 날짜 및 시간 정보를 새로 고치도록 하여 일부 업데이트 기회를 보존할 수 있습니다.
>




**Show content quickly.** When you determine the update frequency that fits with the data you display, you don’t need to hide stale data behind placeholder content.
> 내용을 빨리 표시합니다. 표시하는 데이터에 맞는 업데이트 빈도를 결정할 때 오래된 데이터를 자리 표시자 내용 뒤에 숨길 필요가 없습니다.
>




# **Interactivity**

In some cases, people need to edit a widget to ensure it displays the information that’s most useful for them. For example, people choose a stock symbol for a Stocks Symbol widget. In contrast, some widgets — like the Podcasts widget — automatically display recent content, so people don’t need to customize them.
> 경우에 따라 사용자는 위젯을 편집하여 가장 유용한 정보를 표시해야 합니다. 예를 들어, 사람들은 주식 기호 위젯에 대한 주식 기호를 선택합니다. 대조적으로 팟캐스트 위젯과 같은 일부 위젯은 최근 내용을 자동으로 표시하므로 사용자가 사용자 정의할 필요가 없습니다.
>




**Make editable widgets easy for people to customize.** If your widget is editable, avoid requiring too many settings or asking for information that might be hard for people to find. You don’t have to design an editing-mode user interface for your widget because the system automatically generates it for you. For developer guidance, see [Making a configurable widget](https://developer.apple.com/documentation/widgetkit/making-a-configurable-widget).
> 편집 가능한 위젯을 사용자가 쉽게 사용자 지정할 수 있도록 합니다. 위젯을 편집할 수 있는 경우 너무 많은 설정을 요구하거나 사용자가 찾기 어려운 정보를 요청하지 않도록 합니다. 위젯이 자동으로 생성되므로 위젯에 대한 편집 모드 사용자 인터페이스를 설계할 필요가 없습니다. 개발자 지침은 구성 가능한 위젯 만들기를 참조하십시오.
>




**Ensure that a widget interaction opens your app at the right location.**When people interact with your widget, it deep links into your app, where you can offer details and actions that directly relate to the widget’s content. Avoid making people navigate to the relevant area. For example, when people click or tap a Stocks Symbol widget, the Stocks app opens to a page that displays information about that symbol. Similarly, when people click or tap a small Stocks Watchlist widget, the app opens to show the complete watchlist. When people click or tap one symbol in a larger version of the Watchlist widget, Stocks open to show that symbol.
> 위젯 상호 작용을 통해 올바른 위치에서 앱이 열리는지 확인합니다.사용자가 위젯과 상호 작용하면 앱에 깊이 연결되어 위젯의 내용과 직접 관련된 세부 정보와 작업을 제공할 수 있습니다. 사용자가 관련 영역으로 이동하지 않도록 합니다. 예를 들어 사람들이 주식 기호 위젯을 클릭하거나 탭하면 주식 앱이 열리고 해당 기호에 대한 정보가 표시되는 페이지가 나타납니다. 마찬가지로, 사람들이 작은 주식 감시 목록 위젯을 클릭하거나 탭하면 앱이 열리고 전체 감시 목록이 표시됩니다. 더 큰 버전의 감시 목록 위젯에서 사용자가 하나의 기호를 누르거나 누르면 해당 기호를 표시하기 위해 재고가 열립니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/multiple-tap-targets_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/multiple-tap-targets_2x.png)

**Avoid defining too many interaction targets.** A small widget supports a single target, but larger widgets can offer multiple targets. For example, the medium Notes widget can display several notes. When people click or tap one of them, the app opens to display that note. Although multiple interaction targets might make sense for your content, avoid offering so many that people have to spend time choosing the one they want.
> 너무 많은 상호 작용 대상을 정의하지 마십시오. 작은 위젯은 단일 대상을 지원하지만 큰 위젯은 여러 대상을 제공할 수 있습니다. 예를 들어, 중간 크기의 Notes 위젯은 여러 노트를 표시할 수 있습니다. 사람들이 그들 중 하나를 클릭하거나 탭하면, 그 노트를 표시하기 위해 앱이 열립니다. 여러 개의 상호작용 대상이 내용에 적합할 수 있지만, 너무 많이 제공하여 사람들이 원하는 대상을 선택하는 데 시간을 할애하지 않도록 하십시오.
>




**Let people know when authentication adds value.** If your widget provides additional functionality when someone is signed in to your app, make sure people know that. For example, an app that shows upcoming reservations might include a message like “Sign in to view reservations” when people are signed out.
> 인증이 가치를 추가할 때 사용자에게 알려줍니다. 다른 사용자가 앱에 로그인했을 때 위젯이 추가 기능을 제공하는 경우 사용자가 이를 알 수 있도록 합니다. 예를 들어, 예정된 예약을 보여주는 앱에는 사용자가 로그아웃할 때 "예약을 보려면 로그인"과 같은 메시지가 포함될 수 있습니다.
>




# **Interface design**

Widgets use vivid colors, rich images, and clear, crisp text that’s easy to read at a glance. A unique, beautiful widget not only provides useful information, it also can encourage people to feature it on their devices.
> 위젯은 선명한 색상, 풍부한 이미지, 한눈에 읽기 쉬운 선명하고 선명한 텍스트를 사용합니다. 독특하고 아름다운 위젯은 유용한 정보를 제공할 뿐만 아니라 사람들이 기기에 그것을 사용하도록 장려할 수 있다.
>




**Help people recognize your widget by including design elements linked to your brand’s identity.** Design elements like brand colors, typeface, and stylized glyphs can make a widget instantly recognizable. Take care to keep brand-related design elements from crowding out useful information or making your widget look out of place on the Home Screen.
> 브랜드의 아이덴티티에 연결된 디자인 요소를 포함하여 사람들이 위젯을 인식할 수 있도록 지원합니다. 브랜드 색상, 서체 및 양식화된 글리프와 같은 디자인 요소를 사용하면 위젯을 즉시 인식할 수 있습니다. 브랜드 관련 디자인 요소가 홈 스크린에서 유용한 정보를 대량으로 제공하거나 위젯이 어울리지 않게 보이지 않도록 주의하십시오.
>




**NOTE**When a widget appears in Notification Center in macOS or on the Home Screen in iOS, the system displays the app name below it. In Today View, the Lock Screen on iPhone, and the Home Screen in iPadOS, the app name doesn’t appear below a widget.
> 참고 위젯이 macOS의 Notification Center 또는 iOS의 홈 화면에 나타나면 시스템은 그 아래에 앱 이름을 표시합니다. Today View, iPhone의 잠금 화면 및 iPadOS의 홈 화면에서는 위젯 아래에 앱 이름이 표시되지 않습니다.
>




**Consider carefully before displaying a logo, wordmark, or app icon in your widget.** When you include brand-related design elements like colors and fonts, people seldom need your logo or app icon to help them recognize your widget. Also, the widget gallery displays your app name and icon when it lists the various types and sizes of widgets you offer. In some widgets — for example, those that display content from multiple sources — it may make sense to include a small logo in the top-right corner to subtly identify the app that provides the widget.
> 로고, 워드마크 또는 앱 아이콘을 위젯에 표시하기 전에 신중하게 고려하십시오. 색상 및 글꼴과 같은 브랜드 관련 디자인 요소를 포함할 때 위젯을 인식하는 데 도움이 되는 로고나 앱 아이콘이 필요한 경우는 거의 없습니다. 또한 위젯 갤러리는 사용자가 제공하는 다양한 위젯 유형 및 크기를 나열할 때 사용자의 앱 이름과 아이콘을 표시합니다. 일부 위젯(예: 여러 소스의 콘텐츠를 표시하는 위젯)에서는 오른쪽 상단 모서리에 작은 로고를 포함하여 위젯을 제공하는 앱을 미묘하게 식별할 수 있습니다.
>




**Aim for a comfortable density of information.** When content appears sparse, the widget can seem unnecessary; when content is too dense, the widget isn’t glanceable. If you have lots of information to include, avoid letting your widget become a collage of items that are difficult to parse. Seek ways to curate the content so that people can grasp the essential parts instantly and view relevant details at a longer look. You might also consider creating a larger widget and looking for places where you can replace text with graphics without losing clarity.
> 편안한 정보 밀도를 목표로 합니다. 콘텐츠가 희박하게 나타날 때 위젯이 불필요해 보일 수 있습니다. 콘텐츠가 너무 밀도가 높으면 위젯을 한눈에 볼 수 없습니다. 포함할 정보가 많은 경우 위젯이 구문 분석하기 어려운 항목의 콜라주가 되지 않도록 하십시오. 사람들이 중요한 부분을 즉시 파악하고 관련 세부 사항을 더 길게 볼 수 있도록 내용을 큐레이션하는 방법을 모색합니다. 더 큰 위젯을 만들고 명확성을 잃지 않고 텍스트를 그래픽으로 바꿀 수 있는 위치를 찾는 것도 고려할 수 있습니다.
>




**Use color judiciously.** Beautiful colors draw the eye, but they’re best when they don’t prevent people from absorbing a widget’s information at a glance. Use color to enhance a widget’s appearance without competing with its content. In your asset catalog, you can also specify the colors you want the system to use as it generates your widget’s editing-mode user interface.
> 색상을 신중하게 사용하십시오. 아름다운 색상은 눈길을 끌지만 위젯의 정보를 한 눈에 파악하는 데 방해가 되지 않을 때 가장 좋습니다. 색상을 사용하여 위젯의 내용과 경쟁하지 않고 위젯의 모양을 향상시킵니다. 자산 카탈로그에서 위젯의 편집 모드 사용자 인터페이스를 생성할 때 시스템에서 사용할 색상을 지정할 수도 있습니다.
>




**Support Dark Mode.** Ideally, a widget looks great in both the light and dark appearances. In general, avoid displaying dark text on a light background for the dark appearance, or light text on a dark background for the light appearance. When you use the semantic system colors for text and backgrounds, the colors dynamically adapt to the current appearance. You can also support different appearances by putting color variants in your asset catalog. For guidance, see [Dark Mode](../foundations/dark-mode); see [Asset management](https://developer.apple.com/documentation/xcode/asset-management) and [Supporting Dark Mode in your interface](https://developer.apple.com/documentation/uikit/appearance_customization/supporting_dark_mode_in_your_interface).
> 다크 모드를 지원합니다. 이상적인 경우 위젯은 밝은 모양과 어두운 모양 모두에 적합합니다. 일반적으로 어두운 배경에는 어두운 텍스트를 표시하거나 밝은 배경에는 밝은 텍스트를 표시하지 마십시오. 텍스트 및 배경에 시맨틱 시스템 색상을 사용하면 색상이 현재 모양에 동적으로 적용됩니다. 또한 자산 카탈로그에 색상 변형을 넣어 다양한 모양을 지원할 수 있습니다. 자세한 내용은 다크 모드를 참조하십시오. 인터페이스에서 자산 관리 및 지원 다크 모드를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/notes-small-light_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/notes-small-light_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/notes-small-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/notes-small-dark_2x.png)

**Consider using the system font and SF Symbols.** Using the system font helps your widget look at home on any platform, while making it easier for you to display great-looking text in a variety of weights, styles, and sizes. Use SF Symbols to align and scale symbols with text that uses the system font. If you need to use a custom font, consider using it sparingly, and be sure it’s easy for people to read at a glance. It often works well to use a custom font for the large text in a widget and SF Pro for the smaller text. For guidance, see [Typography](../foundations/typography) and [SF Symbols](../foundations/sf-symbols).
> 시스템 글꼴 및 SF 기호를 사용하는 것을 고려해 보십시오. 시스템 글꼴을 사용하면 위젯이 모든 플랫폼에서 집을 보는 데 도움이 되며 다양한 무게, 스타일 및 크기로 보기 좋은 텍스트를 쉽게 표시할 수 있습니다. SF 기호를 사용하여 기호를 시스템 글꼴을 사용하는 텍스트와 정렬하고 축척합니다. 사용자 정의 글꼴을 사용해야 하는 경우 사용자 정의 글꼴을 사용하지 말고 사용자가 쉽게 한 눈에 볼 수 있도록 하십시오. 위젯의 큰 텍스트에는 사용자 정의 글꼴을 사용하고 작은 텍스트에는 SF Pro를 사용하는 것이 좋습니다. 자세한 내용은 타이포그래피 및 SF 기호를 참조하십시오.
>




**Avoid using very small font sizes.** In general, display text using fonts at 11 points or larger. Text in a font that’s smaller than 11 points can be too small for most people to read at a glance.
> 글꼴 크기가 매우 작으면 안 됩니다. 일반적으로 글꼴을 11포인트 이상 사용하여 텍스트를 표시합니다. 11포인트보다 작은 글꼴의 텍스트는 너무 작아서 대부분의 사용자가 한 눈에 볼 수 없습니다.
>




**Always use text elements in a widget to ensure that your text scales well.** In particular, don’t rasterize text — doing so prevents VoiceOver from speaking your content.
> 위젯의 텍스트 요소를 항상 사용하여 텍스트 크기를 적절하게 조정하십시오. 특히 텍스트를 래스터화하지 마십시오. 이렇게 하면 VoiceOver에서 내용을 말할 수 없습니다.
>




**Design a realistic preview to display in the widget gallery.** Highlighting your widget’s capabilities — and clearly representing the experiences each widget type or size can provide — helps people make an informed decision. You can display real data in your widget preview, but if the data takes too long to generate or load, display realistic simulated data instead.
> 위젯 갤러리에 표시할 사실적인 미리보기를 설계합니다. 위젯의 기능을 강조하고 각 위젯 유형 또는 크기가 제공할 수 있는 경험을 명확하게 나타내면 정보에 입각한 결정을 내리는 데 도움이 됩니다. 위젯 미리보기에 실제 데이터를 표시할 수 있지만 데이터를 생성하거나 로드하는 데 너무 오래 걸리는 경우에는 실제 시뮬레이션 데이터를 대신 표시합니다.
>




**Design placeholder content that helps people recognize your widget.**An installed widget displays placeholder content while its data loads. You can create an effective placeholder appearance by combining static interface components with semi-opaque shapes that stand in for dynamic content. For example, you can use rectangles of different widths to suggest lines of text, and circles or squares in place of glyphs and images.
> 사람들이 위젯을 인식할 수 있도록 도와주는 플레이스홀더 내용을 설계합니다.설치된 위젯은 데이터를 로드하는 동안 자리 표시자 콘텐츠를 표시합니다. 정적 인터페이스 구성요소를 동적 내용을 나타내는 반투명 모양과 결합하여 효과적인 자리 표시자 모양을 만들 수 있습니다. 예를 들어, 너비가 다른 직사각형을 사용하여 문자의 선을 제안하고 글리프와 이미지 대신 원 또는 사각형을 제안할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/tips-placeholder_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/tips-placeholder_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/tips_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/tips_2x.png)

**Avoid mirroring your widget’s appearance within your app.** If your app displays an element that looks like your widget but doesn’t behave like it, people can be confused when the element responds differently when they interact with it. Also, people may be less likely to try other ways to interact with such an element in your app because they expect it to behave like a widget.
> 앱에서 위젯 모양을 미러링하지 않도록 합니다. 위젯과 유사하지만 동작이 다른 요소를 표시하는 경우 해당 요소와 상호 작용할 때 다른 반응을 보일 때 사람들이 혼동할 수 있습니다. 또한, 사람들은 위젯처럼 동작할 것으로 예상하기 때문에 앱에서 이러한 요소와 상호 작용하기 위한 다른 방법을 시도할 가능성이 적을 수 있습니다.
>




**Write a succinct description of your widget.** The widget gallery displays descriptions that help people understand what each widget does. It generally works well to begin a description with an action verb — for example, “See the current weather conditions and forecast for a location” or “Keep track of your upcoming events and meetings.” Avoid including unnecessary phrases that reference the widget itself, like “This widget shows...,” “Use this widget to...,” or “Add this widget.” Use approachable language and [sentence-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64).
> 위젯에 대한 간단한 설명을 작성합니다. 위젯 갤러리에는 각 위젯의 기능을 이해하는 데 도움이 되는 설명이 표시됩니다. 일반적으로 작업 동사로 설명을 시작하는 것이 좋습니다. 예를 들어 "현재 날씨 상태 및 위치 예측 보기" 또는 "예정된 이벤트 및 회의를 추적하십시오."입니다. 위젯 자체를 참조하는 불필요한 구(예: "이 위젯 표시...", "이 위젯을 사용하여..." 또는 "이 위젯 추가")는 포함하지 마십시오. 접근 가능한 언어와 문장 스타일의 대문자를 사용합니다.
>




**Group your widget’s sizes together, and provide a single description.** If your widget is available in multiple sizes, group the sizes together so people don’t think each size is a different widget. Provide a single description of your widget — regardless of how many sizes you offer — to avoid repetition and to help people understand how each size provides a slightly different perspective on the same content and functionality.
> 위젯의 크기를 그룹화하고 하나의 설명을 제공합니다. 위젯의 크기가 여러 개인 경우 크기를 그룹화하여 사용자가 각 크기를 다른 위젯이라고 생각하지 않도록 합니다. 제공하는 크기에 관계없이 위젯에 대한 단일 설명을 제공하여 반복을 방지하고 각 크기가 동일한 내용과 기능에 대해 어떻게 다른 관점을 제공하는지 이해할 수 있도록 합니다.
>




**Consider coloring the Add button.** After people choose your app in the widget gallery, an Add button appears below the group of widgets you offer. You can specify a color for this button to help remind people of your brand.
> 위젯 갤러리에서 사용자의 앱을 선택하면 제공하는 위젯 그룹 아래에 추가 단추가 나타납니다. 이 단추의 색상을 지정하여 사용자의 브랜드를 알릴 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/add-button-custom-color-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/add-button-custom-color-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/add-button-custom-color-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/add-button-custom-color-2_2x.png)

# **Adapting to different screen sizes**
> 다양한 화면 크기에 맞게 조정
>




Widgets scale to adapt to the screen sizes of different devices and onscreen areas. Ensure that your widget looks great on every device by supplying content at appropriate sizes.
> 위젯은 다양한 장치 및 화면 영역의 화면 크기에 맞게 확장됩니다. 콘텐츠를 적절한 크기로 제공하여 모든 장치에서 위젯이 잘 보이도록 합니다.
>




**Design content to look great on all devices and scale factors, letting the system resize or scale as necessary.** In iOS, the system ensures that your widget looks good on small devices by resizing the content you design for large devices. In iPadOS, the system renders your widget at a large size before scaling it down for display on the Home Screen. As you create design comprehensives for various devices and scale factors, use the values listed in [Specifications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets#specifications) for guidance; for your production widget, use [SwiftUI](https://developer.apple.com/documentation/SwiftUI) to ensure flexibility.
> 모든 장치와 스케일 팩터에서 보기 좋게 컨텐츠를 디자인합니다. 필요에 따라 시스템 크기를 조정하거나 조정할 수 있습니다. iOS에서 시스템은 대형 장치용으로 디자인한 컨텐츠의 크기를 조정하여 소형 장치에서 위젯이 보기 좋게 보이도록 합니다. iPadOS에서 시스템은 홈 스크린에 표시하기 위해 위젯을 축소하기 전에 위젯을 큰 크기로 렌더링합니다. 다양한 장치 및 스케일 팩터에 대한 설계 종합을 생성할 때 사양에 나열된 값을 지침으로 사용하고 프로덕션 위젯의 경우 Swift를 사용합니다.UI를 통해 유연성을 보장합니다.
>




**Coordinate the corner radius of your content with the corner radius of the widget.** To ensure that your content looks good within a widget’s rounded corners, use a SwiftUI container to apply the correct corner radius. For developer guidance, see [ContainerRelativeShape](https://developer.apple.com/documentation/swiftui/containerrelativeshape).
> 콘텐츠의 모서리 반지름을 위젯의 모서리 반지름과 조정합니다. 위젯의 둥근 모서리 내에서 콘텐츠가 잘 보이도록 하려면 Swift를 사용하십시오.올바른 모서리 반지름을 적용하기 위한 UI 컨테이너입니다. 개발자 지침은 컨테이너 상대 모양을 참조하십시오.
>




**NOTE**In iOS, widgets support [Dynamic Type sizes](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#specifications) from Large to AX5 when you use [Font](https://developer.apple.com/documentation/swiftui/font) to choose a system font or [custom(_:size:)](https://developer.apple.com/documentation/swiftui/font/custom(_:size:)) to choose a custom font.
> 참고 iOS에서 위젯은 글꼴을 사용하여 시스템 글꼴을 선택하거나 사용자 정의 글꼴을 선택하기 위해 사용자 정의(_:size:))할 때 동적 유형 크기를 지원합니다.
>




**In general, use standard margins to ensure your content is comfortably legible.** The standard margin width is 16 points. If your widget displays content like text, glyphs, and graphs, use the standard margins to avoid crowding the edges and creating a cluttered appearance. For developer guidance, see [padding(`_:`_:)](https://developer.apple.com/documentation/swiftui/view/padding(_:_:)). If you use background shapes to create visual content groupings, or if you display button backgrounds, you might need to use tight margins. Tight margins — which measure 11 points in width — can also help make graphics that contain information easier for people to read.
> 일반적으로 내용이 읽기 쉽도록 표준 여백을 사용하십시오. 표준 여백 폭은 16포인트입니다. 위젯에서 텍스트, 글리프 및 그래프와 같은 내용을 표시하는 경우 가장자리가 혼잡하거나 모양이 흐트러지지 않도록 표준 여백을 사용합니다. 개발자 지침은 패딩(`_:`_:)을 참조하십시오. 배경 모양을 사용하여 시각적 내용 그룹을 만들거나 단추 배경을 표시하는 경우 여백을 좁게 표시해야 할 수 있습니다. 너비가 11포인트인 좁은 여백은 사람들이 정보를 포함하는 그래픽을 더 쉽게 읽을 수 있도록 도와줄 수도 마찬가지입니다.
>




# **Platform considerations**

*No additional considerations for iPadOS or macOS. Not supported in tvOS or watchOS.*
> iPad에 대한 추가 고려 사항 없음OS 또는 macOS. TVOS 또는 워치에서 지원되지 않음운영 체제
>




# **iOS**

Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for [complications](../components/system-experiences/complications/) in addition to design principles for widgets. Both support Always-On display and emphasize glanceable content within their limited space. Provide useful information in your Lock Screen widget, and don’t treat it only as an additional way for people to launch into your app. Additionally, the vibrant rendering mode that widgets on the Lock Screen use is similar to the accented rendering mode for watch complications because they both communicate information without relying on color only. In many cases, a design for complications also works well for widgets on the Lock Screen (and vice versa), so consider creating them in tandem.
> 잠금 화면의 위젯은 기능적으로 복잡도를 관찰하는 것과 유사하며 위젯의 설계 원칙 외에도 복잡도에 대한 설계 원칙을 따릅니다. 둘 다 Always-On 디스플레이를 지원하며 제한된 공간 내에서 눈에 띄는 콘텐츠를 강조합니다. 잠금 화면 위젯에 유용한 정보를 제공하고, 사용자가 앱을 실행하는 추가적인 방법으로만 취급하지 마십시오. 또한 잠금 화면의 위젯이 사용하는 선명한 렌더링 모드는 색상에만 의존하지 않고 정보를 전달하기 때문에 시계 복잡성에 대한 악센트 렌더링 모드와 유사합니다. 대부분의 경우, 복잡한 설계는 잠금 화면의 위젯에도 잘 적용되므로, 함께 작성하는 것을 고려해 보십시오.
>




Your app can offer widgets on the Lock Screen in three different shapes: as inline text that appears above the clock and circular and rectangular shapes that appear below the clock.
> 앱은 잠금 화면에 시계 위에 나타나는 인라인 텍스트와 시계 아래에 나타나는 원형 및 직사각형 모양의 세 가지 모양으로 위젯을 제공할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/weather-widget-lock-screen_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/weather-widget-lock-screen_2x.png)

As with complications, aim to create widgets on the Lock Screen that are informative, dynamic, and display up-to-date information.
> 복잡한 경우와 마찬가지로 잠금 화면에 정보를 제공하고 동적이며 최신 정보를 표시하는 위젯을 만드는 것을 목표로 합니다.
>




**Adjust colors and images for the vibrant rendering mode.** The system renders widgets on the Lock Screen using a vibrant, blurred appearance. The opacity of pixels within your image determines the strength of the blurred material effect. Fully transparent pixels let the background wallpaper pass through as is. When creating assets for the Lock Screen, render content like images, numbers, or text at full opacity. The brightness of pixels determines how vibrant they appear on the Lock Screen: Brighter gray values provide more contrast, and darker values provide less contrast. To establish hierarchy, use white or light gray for the most prominent content and darker grayscale values for secondary elements.
> 선명한 렌더링 모드에 맞게 색상과 이미지를 조정합니다. 시스템은 선명하고 흐릿한 모양을 사용하여 잠금 화면에서 위젯을 렌더링합니다. 이미지 내 픽셀의 불투명도에 따라 흐릿한 재료 효과의 강도가 결정됩니다. 완전히 투명한 픽셀은 배경 벽지를 그대로 통과하게 한다. 잠금 화면에 대한 자산을 만들 때 이미지, 숫자 또는 텍스트와 같은 내용을 최대 불투명도로 렌더링합니다. 픽셀의 밝기에 따라 잠금 화면에 선명하게 표시되는 정도가 결정됩니다. 회색 값이 밝으면 더 큰 대비를 제공하고 어두운 값은 더 적은 대비를 제공합니다. 계층을 설정하려면 가장 눈에 띄는 내용에는 흰색 또는 밝은 회색을 사용하고 보조 요소에는 어두운 회색 척도 값을 사용하십시오.
>




To make sure images look great in the vibrant rendering mode:
> 선명한 렌더링 모드에서 이미지가 멋지게 보이도록 하려면:
>




- Confirm that your images' content has sufficient contrast in grayscale.
- >  이미지 내용의 대비가 회색조로 충분한지 확인합니다.

- Use opaque grayscale values, rather than opacities of white, to achieve the best vibrant material effect.
- >  흰색의 불투명도 대신 불투명 그레이스케일 값을 사용하면 최상의 선명한 재료 효과를 얻을 수 있습니다.


**Support Always-On display.** Devices with Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in Always-On display, and make sure your content is legible.
> Always-On 디스플레이 지원. Always-On 디스플레이가 있는 장치는 잠금 화면에 위젯을 렌더링하여 휘도를 낮춥니다. Always-On 디스플레이에서 충분한 대비를 제공하는 회색 수준을 사용하고 내용을 읽을 수 있는지 확인합니다.
>




For developer guidance, see [Creating Lock Screen widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating-lock-screen-widgets-and-watch-complications), [WidgetRenderingMode](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode), and [vibrant](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/vibrant).
> 개발자 지침은 잠금 화면 위젯 작성 및 복잡한 화면 보기, 위젯 렌더링 모드 및 선명한 화면 보기를 참조하십시오.
>




# **Specifications**

# **iOS widget design comprehensives**

| Screen size (portrait, pts) | Small (pts) | Medium (pts) | Large (pts) | Circular (pts) | Rectangular (pts) | Inline (pts) |
| --- | --- | --- | --- | --- | --- | --- |
| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |
| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |
| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |
| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 320x568 | 141x141 | 292x141 | 292x311 | n/a | n/a | n/a |

# **iPadOS widget design comprehensives**

| Screen size (portrait, pts) | Target | Small (pts) | Medium (pts) | Large (pts) | Extra large (pts) |
| --- | --- | --- | --- | --- | --- |
| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| Device | 120x120 | 260x120 | 260x260 | 540x260 |  |
| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| Device | 120x120 | 260x120 | 260x260 | 540x260 |  |
| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |
| Device | 124x124 | 272x124 | 272x272 | 568x272 |  |
| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| Device | 136x136 | 300x136 | 300x300 | 628x300 |  |
| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |
| Device | 132x132 | 288x132 | 288x288 | 600x288 |  |
| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| Device | 136x136 | 300x136 | 300x300 | 628x300 |  |
| 954x1373 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| Device | 162x162 | 350x162 | 350x350 | 726x350 |  |
| 970x1389 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| Device | 162x162 | 350x162 | 350x350 | 726x350 |  |
| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |
| Device | 160x160 | 356x160 | 356x356 | 748x356 |  |
| 1192x1590 * | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |
| Device | 188x188 | 412x188 | 412x412 | 860x412 |  |
- When Display Zoom is set to More Space.
- >  디스플레이 확대/축소가 추가 공간으로 설정된 경우.

