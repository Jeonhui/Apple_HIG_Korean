# **[components-status] home-screen-quick-actions**

## Home Screen quick actions give people a way to perform app-specific actions from the Home Screen.
> 홈 스크린 빠른 작업은 사용자가 홈 스크린에서 앱별 작업을 수행할 수 있는 방법을 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/home-screen-quick-actions-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/home-screen-quick-actions-intro-dark_2x.png)

People can get a menu of available quick actions when they touch and hold an app icon (on a 3D Touch device, people can press on the icon with increased pressure to see the menu). For example, Mail includes quick actions that open the Inbox or the VIP mailbox, initiate a search, and create a new message. In addition to app-specific actions, a Home Screen quick action menu also lists items for removing the app and editing the Home Screen.
> 사람들은 앱 아이콘을 길게 터치할 때 사용 가능한 빠른 동작의 메뉴를 얻을 수 있다(3D Touch 장치에서, 사람들은 메뉴를 보기 위해 증가된 압력으로 아이콘을 누를 수 있다). 예를 들어, 메일에는 받은 문서 또는 VIP 사서함을 열고 검색을 시작하고 새 메시지를 작성하는 빠른 수행이 포함되어 있습니다. 앱별 작업 외에도 홈 스크린 빠른 작업 메뉴에는 앱을 제거하고 홈 스크린을 편집하기 위한 항목도 나열됩니다.
>




Each Home Screen quick action includes a title, an interface icon on the left or right (depending on your app’s position on the Home Screen), and an optional subtitle. The title and subtitle are always left-aligned in left-to-right languages. Your app can even dynamically update its quick actions when new information is available. For example, Messages provides quick actions for opening your most recent conversations.
> 각 홈 스크린 빠른 작업에는 제목, 왼쪽 또는 오른쪽의 인터페이스 아이콘(홈 화면에서 앱의 위치에 따라 다름) 및 선택적 부제가 포함됩니다. 제목과 부제는 항상 왼쪽에서 오른쪽으로 정렬됩니다. 새로운 정보를 사용할 수 있을 때 앱은 빠른 작업을 동적으로 업데이트할 수도 있습니다. 예를 들어, 메시지는 가장 최근의 대화를 열기 위한 빠른 작업을 제공합니다.
>




# **Best practices**

**Create quick actions for compelling, high-value tasks.** For example, Maps lets people search near their current location or get directions home without first opening the Maps app. Every app should enable at least one useful quick action; you can provide a total of four.
> 지도를 사용하면 사람들이 먼저 지도 앱을 열지 않고도 현재 위치 근처를 검색하거나 집으로 가는 길을 찾을 수 있습니다. 모든 앱은 적어도 하나의 유용한 빠른 작업을 활성화해야 하며, 총 4개를 제공할 수 있습니다.
>




**Avoid making unpredictable changes to quick actions.** Dynamic quick actions are a great way to keep actions relevant. For example, it may make sense to update quick actions based on the current location or recent activities in your app, time of day, or changes in settings. However, actions shouldn’t change in ways that are unpredictable or confusing.
> 빠른 작업에 대해 예측할 수 없는 변경을 하지 않도록 합니다. 동적 빠른 작업은 작업을 관련성 있게 유지하는 좋은 방법입니다. 예를 들어, 앱의 현재 위치 또는 최근 활동, 시간 또는 설정 변경에 따라 빠른 작업을 업데이트하는 것이 적절할 수 있습니다. 하지만, 행동은 예측할 수 없거나 혼란스러운 방식으로 바뀌어서는 안 됩니다.
>




**Provide a succinct title for each quick action.** An action’s title should instantly communicate the results of the action; for example, “Directions Home,” “Create New Contact,” and “New Message.” If you need to give more context, provide a subtitle too. Mail uses subtitles to indicate whether there are unread messages in the Inbox and VIP folder. Don’t include your app name or any extraneous information in the title or subtitle, keep the text short to avoid truncation, and take localization into account as you write the text.
> 각 빠른 수행에 대한 간략한 제목을 제공하십시오. 수행의 제목은 "방향 홈", "새 연락처 만들기" 및 "새 메시지"와 같이 수행 결과를 즉시 전달해야 합니다. 만약 당신이 더 많은 문맥을 제공할 필요가 있다면, 부제도 제공하세요. 메일은 받은 문서 및 VIP 폴더에 읽지 않은 메시지가 있는지 여부를 나타내기 위해 자막을 사용합니다. 앱 이름이나 관련 없는 정보를 제목이나 부제에 포함시키지 말고, 잘라내기를 방지하기 위해 텍스트를 짧게 유지하고, 텍스트를 작성할 때 현지화를 고려하십시오.
>




**Provide a recognizable interface icon for each quick action.** Consider using an [SF Symbol](../foundations/sf-symbols) to represent an action. If you design your own interface [icons](../foundations/icons), use the Quick Action Icon Template that’s included with [Apple Design Resources for iOS and iPadOS](https://developer.apple.com/design/resources/#ios-apps) and use the following sizes for guidance.
> 각 빠른 동작에 대해 인식 가능한 인터페이스 아이콘을 제공하십시오. 동작을 나타내기 위해 SF 기호를 사용하는 것을 고려해 보십시오. 인터페이스 아이콘을 직접 디자인하는 경우 iOS 및 iPadOS용 Apple Design Resources에 포함된 빠른 작업 아이콘 템플릿을 사용하고 다음 크기를 사용하여 지침을 따르십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/max-width-height.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/max-width-height.svg)

Maximum width and height

---

34.67x34.67 pt (104x104 px @3x)

---

35x35 pt (70x70 px @2x)

---

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width-height.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width-height.svg)

Target width and height

---

26.67x26.67 pt (80x80 px @3x)

---

27x27 pt (54x54 px @2x)

---

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-width.svg)

Target width (wide glyphs)

---

29.33pt (88px @3x)

---

30pt (60px @2x)

---

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-height.svg](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/home-screen-quick-actions/images/target-height.svg)

Target height (tall glyphs)

---

29.33pt (88px @3x)

---

30pt (60px @2x)

---

**Don’t use an emoji in place of a symbol or interface icon.** Emojis are full color, whereas quick action symbols are monochromatic and change appearance in Dark Mode to maintain contrast.
> 빠른 동작 기호는 단색이며 대비를 유지하기 위해 다크 모드에서 모양을 변경하는 반면, 기호나 인터페이스 아이콘 대신 이모지를 사용하지 마십시오.
>




# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in macOS, watchOS, or tvOS.*
> iOS 또는 iPadOS에 대한 추가 고려 사항은 없습니다. macOS, watchOS 또는 tvOS에서는 지원되지 않습니다.
>



