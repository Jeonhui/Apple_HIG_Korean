# **[technologies-siri] shortcuts-and-suggestions**

When you support shortcuts, people have a variety of ways to discover and interact with the custom and system intents your app provides. For example:
> 바로 가기를 지원하면 앱에서 제공하는 사용자 지정 및 시스템 의도를 검색하고 상호 작용할 수 있는 다양한 방법이 있습니다. 예:
>




- Siri can suggest a shortcut for an action people have performed at least once by offering it in search results, on the lock screen, and in the Shortcuts app.
- >  Siri는 검색 결과, 잠금 화면 및 바로 가기 앱에서 사람들이 한 번 이상 수행한 작업에 대한 바로 가기를 제안할 수 있습니다.

- Your app can supply a shortcut for an action that people haven’t done yet, but might want to do in the future, so that the Shortcuts app can suggest it or it can appear on the [Siri watch face](https://support.apple.com/guide/watch/faces-and-features-apde9218b440/watchos#apdcc88df92c).
- >  당신의 앱은 사람들이 아직 하지 않았지만 미래에 하고 싶어할 수 있는 작업에 대한 바로 가기를 제공하여 바로 가기 앱이 제안하거나 Siri 워치 페이스에 나타날 수 있다.

- People can use the Shortcuts app to view all their shortcuts and even combine actions from different apps into multistep shortcuts.
- >  바로 가기 앱을 사용하여 모든 바로 가기를 볼 수 있으며 다양한 앱의 작업을 여러 단계의 바로 가기로 결합할 수도 있습니다.

- People can also use the Shortcuts app to automate a shortcut by defining the conditions that should run it, like time of day or current location.
- >  또한 바로 가기 앱을 사용하여 바로 가기를 실행해야 하는 조건(예: 시간 또는 현재 위치)을 정의하여 바로 가기를 자동화할 수 있습니다.

- When you provide an Add to Siri button for your custom intent, people can create a shortcut they can run with their voice (for guidance, see [Help people add shortcuts](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#help-people-add-shortcuts)).
- >  사용자 지정 용도에 맞게 Siri에 추가 단추를 제공하면 사용자가 음성으로 실행할 수 있는 바로 가기를 만들 수 있습니다(참고 사항은 바로 가기 추가 도움말 참조).


![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-initial-recording_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-initial-recording_2x.png)

The Shortcuts app is also available in macOS 12 and later and in watchOS 7 and later. For developer guidance, see [SiriKit > Shortcuts](https://developer.apple.com/documentation/sirikit#2979425).
> 바로 가기 앱은 macOS 12 이상 및 watch에서도 사용할 수 있습니다OS 7 이상. 개발자 지침은 SiriKit > 바로 가기를 참조하십시오.
>




# **Make app actions widely available**
> 앱 작업을 널리 사용할 수 있도록 설정
>




*Donating* information about the actions your app supports helps the system offer them to people in various ways, such as:
> 앱이 지원하는 작업에 대한 정보를 기부하면 다음과 같은 다양한 방법으로 사용자에게 제공할 수 있습니다:
>




- In search results
- Throughout the Shortcuts app
- On the lock screen as a Siri Suggestion
- >  잠금 화면에서 Siri 제안 사항으로 표시

- Within the Now Playing view (for recently played media content)
- >  지금 재생 보기 내(최근에 재생한 미디어 콘텐츠의 경우)

- During Wind Down

Donations also power Automation Suggestions in the Shortcut app’s Gallery, making it easy for people to set up automations for hands-free interactions with your app.
> 기부는 또한 바로 가기 앱의 갤러리에 있는 자동화 제안에 힘을 실어주어, 사람들이 앱과의 핸즈프리 상호 작용을 위한 자동화를 쉽게 설정할 수 있게 해준다.
>




You can also tell the system about shortcuts for actions people haven’t taken yet or make a shortcut available on the Siri watch face (for guidance, see [Suggest shortcuts people might want to add to Siri](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#suggest-shortcuts-people-might-want-to-add-to-siri) and [Display Shortcuts on the Siri Watch face](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#display-shortcuts-on-the-siri-watch-face)). For developer guidance, see [Donating shortcuts](https://developer.apple.com/documentation/sirikit/donating_shortcuts).
> 또한 사용자가 아직 수행하지 않은 작업에 대한 바로 가기에 대해 시스템에 알려주거나 Siri Watch Face에서 바로 가기를 사용할 수 있도록 설정할 수 있습니다(자세한 내용은 사용자가 Siri Watch Face에 추가할 수 있는 바로 가기 제안 및 Siri Watch Face의 바로 가기 표시. 개발자 지침은 바로 가기 기부를 참조하십시오.
>




**Make a donation every time people perform the action.** When you donate a shortcut each time people perform the associated action, you help the system more accurately predict the best time and place to offer the shortcut.
> 사람들이 그 행동을 할 때마다 기부를 하세요. 당신이 그 행동을 할 때마다 당신이 바로가기를 기부하면, 당신은 시스템이 바로가기를 제공하기에 가장 좋은 시간과 장소를 더 정확하게 예측할 수 있도록 도와줍니다.
>




**Only donate actions that people actually perform.** For example, a coffee-ordering app should donate the *Order coffee* shortcut every time people order coffee, but it shouldn’t make this donation when people do something else, like browse the menu. Similarly, a media app should donate information about a song — like its title and album — only when people are actually listening to it. (For developer guidance, see [Improving Siri media interactions and app selection](https://developer.apple.com/documentation/sirikit/media/improving_siri_media_interactions_and_app_selection).)
> 예를 들어, 커피 주문 앱은 사람들이 커피를 주문할 때마다 커피 주문 바로 가기를 기부해야 하지만, 사람들이 메뉴를 보는 것과 같은 다른 일을 할 때 이러한 기부를 해서는 안 됩니다. 마찬가지로, 미디어 앱은 사람들이 실제로 노래를 듣고 있을 때만 제목과 앨범과 같은 노래에 대한 정보를 기부해야 합니다. (개발자 지침은 Siri 미디어 상호 작용 및 앱 선택 개선을 참조하십시오.)
>




**Remove donations for actions that require corresponding data.** If information required by a donated action no longer exists, your app should delete the donation so the shortcut isn’t suggested anymore. For example, if people delete a contact in a messaging app, the app should delete donations for messaging that contact. When people create a shortcut themselves, only they can delete it. For developer guidance, see [Deleting Donated Shortcuts](https://developer.apple.com/documentation/sirikit/deleting_donated_shortcuts).
> 해당 데이터가 필요한 작업에 대한 기부를 제거합니다. 기부된 작업에 필요한 정보가 더 이상 존재하지 않으면 앱에서 기부를 삭제해야 더 이상 바로 가기를 제안하지 않습니다. 예를 들어, 사람들이 메시징 앱에서 연락처를 삭제하는 경우, 앱은 해당 연락처를 메시징하기 위한 기부금을 삭제해야 합니다. 사용자가 직접 바로 가기를 만들면 사용자만 바로 가기를 삭제할 수 있습니다. 개발자 지침은 기부된 바로 가기 삭제를 참조하십시오.
>




**If your app handles reservations, consider donating them to the system.** These items — like ticketed events, travel itineraries, or reservations for restaurants, flights, or movies — automatically appear as suggestions in Calendar or Maps. When you donate a reservation, it can appear on the lock screen with a suggestion to check in with your app or as a reminder that uses current traffic conditions to recommend when people should leave. For developer guidance, see [Donating reservations](https://developer.apple.com/documentation/sirikit/siri_event_suggestions/donating_reservations).
> 앱에서 예약을 처리하는 경우 시스템에 해당 예약을 기부하는 것을 고려하십시오. 티켓된 이벤트, 여행 일정 또는 식당, 항공편 또는 영화 예약과 같은 항목은 자동으로 달력 또는 지도에 제안으로 표시됩니다. 예약을 기부하면 잠금 화면에 앱으로 체크인하라는 제안과 함께 표시되거나 현재 교통 상황을 이용해 사람들이 언제 떠나야 하는지를 추천하는 알림으로 표시될 수 있다. 개발자 지침은 예약 기부를 참조하십시오.
>




### **Suggest Shortcuts people might want to add to Siri**
> 사람들이 시리에 추가하고 싶어할 수 있는 바로 가기 제안
>




If your app supports an action that people haven’t performed yet but might find useful, you can provide a *suggested* shortcut to the system so that people can discover it. For example, if people use a coffee-ordering app to order their daily coffee but not to order a holiday special, the app might still want to give them a way to do this with an *Order holiday coffee* shortcut.
> 앱에서 사용자가 아직 수행하지 않았지만 유용하다고 생각할 수 있는 작업을 지원하는 경우 사용자가 시스템을 검색할 수 있도록 시스템에 대한 제안된 바로 가기를 제공할 수 있습니다. 예를 들어, 사람들이 일일 커피를 주문하기 위해 커피 주문 앱을 사용하지만 휴일 스페셜을 주문하지 않는 경우, 앱은 여전히 주문 휴일 커피 바로 가기를 사용하여 이를 수행할 수 있는 방법을 제공할 수 있습니다.
>




Suggested shortcuts appear in both the Gallery and the shortcut editor in the Shortcuts app. Also, your app can display an Add to Siri button that people can use to enable a suggested shortcut while they’re in your app. For developer guidance, see [Suggesting shortcuts to users](https://developer.apple.com/documentation/sirikit/shortcut_management/suggesting_shortcuts_to_users).
> 제안된 바로 가기는 바로 가기 앱의 갤러리와 바로 가기 편집기에 모두 나타납니다. 또한 앱에 사용자가 앱에 있는 동안 제안된 바로 가기를 활성화하는 데 사용할 수 있는 Siri에 추가 버튼을 표시할 수 있습니다. 개발자 지침은 사용자에게 바로 가기 제안을 참조하십시오.
>




### **Display shortcuts on the Siri watch face**
> Siri watch face에 바로 가기
>




On Apple Watch, people can run shortcuts in several ways. For example, people can ask Siri, tap a shortcut [complication](../components/system-experiences/complications/) on a watch face, or use the Shortcuts app available in watchOS 7 and later. You can also make shortcuts available on the Siri watch face.
> Apple Watch에서는 여러 가지 방법으로 바로 가기를 실행할 수 있습니다. 예를 들어, 사람들은 시리에게 물어보거나, 워치 페이스에서 바로 가기 복잡한 것을 탭 하거나, 워치에서 사용할 수 있는 바로 가기 앱을 사용할 수 있다OS 7 이상. 또한 시리 워치 페이스에서 바로 가기를 사용할 수 있습니다.
>




To have a shortcut appear on the Siri watch face, you define a *relevant* shortcut by including information like the time of day at which your shortcut is relevant and how the shortcut should be displayed on the Siri watch face. The information you supply lets the Siri watch face intelligently display your shortcut to people when they’re in the appropriate context.
> Siri watch face에 바로 가기를 표시하려면 바로 가기가 관련된 시간과 Siri watch face에 바로 가기를 표시하는 방법과 같은 정보를 포함하여 관련 바로 가기를 정의합니다. 당신이 제공하는 정보를 통해 시리 워치 페이스는 사람들이 적절한 상황에 있을 때 당신의 바로 가기를 지능적으로 보여준다.
>




For developer guidance, see [Defining relevant shortcuts for your app](https://developer.apple.com/documentation/sirikit/relevant_shortcuts/defining_relevant_shortcuts_for_your_app).
> 개발자 지침은 앱에 대한 관련 바로 가기 정의를 참조하십시오.
>




# **Create shortcut titles and subtitles**
> 바로 가기 제목 및 자막 만들기
>




Shortcut titles and subtitles appear when the system suggests them or when people add shortcuts to Siri or edit them. In Siri Suggestions on iPhone and Apple Watch, a shortcut can also display an image.
> 바로 가기 제목과 자막은 시스템에서 제안할 때 또는 사람들이 시리에 바로 가기를 추가하거나 편집할 때 나타납니다. 아이폰과 애플워치의 '시리 제안'에서 바로가기는 이미지를 표시할 수도 있다.
>




**Be concise but descriptive.** An effective title conveys what happens when the shortcut runs. A subtitle can provide additional detail that supplements — but doesn’t duplicate — the title.
> 간결하지만 서술적이어야 한다. 효과적인 제목은 바로 가기가 실행될 때 일어나는 일을 전달한다. 부제는 제목을 보완하는 추가 세부사항을 제공할 수 있지만 중복되지는 않습니다.
>




**Start titles with a verb and use sentence-style capitalization without punctuation.** Think of a shortcut title as a brief instruction.
> 동사로 제목을 시작하고 문장부호 없이 문장식 대문자를 사용하라. 짧은 제목을 간단한 지시로 생각하라.
>




[제목 없음](https://www.notion.so/554292f08526485aaf9b81a21a8f4fe0)

**Lead with important information.** Long titles and subtitles may be truncated in certain contexts, depending on the device’s screen size.
> 장치의 화면 크기에 따라 특정 상황에서 긴 제목과 자막이 잘릴 수 있습니다.
>




**Exclude your app name.** The system already identifies the app associated with a shortcut.
> 앱 이름을 제외합니다. 시스템에서 바로 가기와 연결된 앱을 이미 식별했습니다.
>




**Localize titles and subtitles.** Providing content in multiple languages ensures an equally great experience for people everywhere.
> 제목과 자막을 현지화합니다. 다국어로 콘텐츠를 제공하면 모든 곳의 사람들에게 동일하게 훌륭한 경험을 보장할 수 있습니다.
>




**Consider providing a custom image for a more engaging suggestion.** For example, the shortcut for *Order my favorite coffee* could show a cup of the customer’s favorite coffee. Create an image that measures:
> 좀 더 매력적인 제안을 위해 사용자 지정 이미지를 제공하는 것을 고려해 보십시오. 예를 들어, 내가 가장 좋아하는 커피 주문의 바로 가기는 고객이 가장 좋아하는 커피 한 잔을 보여줄 수 있습니다. 다음을 측정하는 이미지를 만듭니다:
>




- 60x60 pt (180x180 px @ 3x) to display in an iOS app
- >  iOS 앱에 표시할 60x60pt(180x180px @ 3x)

- 34x34 pt (68x68 px @2x) to display on the Siri watch face on the 44mm Apple Watch (watchOS scales down the image for smaller watches)
- >  44mm Apple Watch의 Siri 워치 페이스에 표시할 34x34pt(68x68px @2x)(시계)OS가 더 작은 시계를 위해 이미지 축소)


# **Help people add shortcuts**

People can add shortcuts from within your app or in the Shortcuts app.
> 앱 내 또는 바로 가기 앱에서 바로 가기를 추가할 수 있습니다.
>




**Offer an Add to Siri button to let people add a shortcut for a common action.** In the Add to Siri sheet that appears when people tap the button, they can type or record a custom voice command (or accept the app’s suggested phrase) and add the shortcut. After the shortcut is added, the button’s text automatically changes to *Added to Siri* and it displays the invocation phrase. These changes show people that they successfully added the shortcut and, crucially, remind them what to say when asking Siri to run it. For guidance on using the Add to Siri button, see [Add to Siri button styles](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#add-to-siri-button-styles).
> Add to Siri 버튼을 제공하여 일반적인 동작에 대한 바로 가기를 추가할 수 있습니다. 버튼을 누르면 나타나는 Add to Siri 시트에서 사용자 지정 음성 명령을 입력하거나 녹음(또는 앱의 제안된 문구를 수락)하고 바로 가기를 추가할 수 있습니다. 단축키가 추가되면 버튼의 텍스트가 자동으로 '시리에 추가됨'으로 바뀌고 호출 문구가 표시된다. 이러한 변화는 사람들이 성공적으로 단축키를 추가했다는 것을 보여주고 결정적으로 시리에게 실행을 요청할 때 할 말을 상기시킨다. Siri에 추가 단추 사용에 대한 지침은 Siri 단추 스타일에 추가를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-not-added_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-not-added_2x.png)

**If you create a custom button to add a shortcut, provide an experience that mirrors the system-provided one.** Display the phrase *Add to Siri* in your custom button. Don’t display alternative phrases — like *add voice command*, *create voice shortcut*, or *make voice prompt* — or display the Siri icon in your custom button. Also, don’t use the Siri icon as a button, or display it anywhere else in your interface. (See [Display multiple shortcuts in one place](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions#display-multiple-shortcuts-in-one-place) for guidance on offering several shortcuts in one screen.)
> 바로 가기를 추가하기 위해 사용자 지정 단추를 만들 경우 시스템에서 제공한 바로 가기를 반영하는 경험을 제공합니다. 사용자 지정 단추에 Siri에 추가 문구를 표시합니다. 음성 명령 추가, 음성 바로 가기 만들기 또는 음성 프롬프트 만들기와 같은 대체 구문을 표시하거나 사용자 지정 단추에 Siri 아이콘을 표시하지 마십시오. 또한 Siri 아이콘을 단추로 사용하거나 인터페이스의 다른 곳에 표시하지 마십시오. 한 화면에 여러 바로 가기를 제공하는 방법에 대한 지침은 한 곳에 여러 바로 가기 표시를 참조하십시오
>




After people use your custom button to add a shortcut, it’s important to display their trigger phrase to help them remember it. If you created a custom Add to Siri button, you can mirror the system-provided experience and update the button to display *Added to Siri* followed by the phrase.
> 사용자 지정 단추를 사용하여 바로 가기를 추가한 후에는 트리거 구문을 표시하여 사용자가 바로 가기를 기억하는 데 도움이 중요합니다. 사용자 정의 시리에 추가 버튼을 만든 경우 시스템에서 제공한 경험을 미러링하고 버튼을 업데이트하여 시리에 추가된 다음 문구를 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-added_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-button-added_2x.png)

**Let people edit and remove the shortcuts they added.** When people tap the trigger phrase displayed in your app after adding a shortcut, show the shortcut editing view again so they can update the phrase or delete the shortcut.
> 사용자가 추가한 바로 가기를 편집하고 제거할 수 있습니다. 바로 가기를 추가한 후 사용자가 앱에 표시된 트리거 구문을 누르면 바로 가기 편집 보기를 다시 표시하여 구문을 업데이트하거나 바로 가기를 삭제할 수 있습니다.
>




**Update the shortcuts your app displays.** People can add, remove, and update your app’s shortcuts in the Shortcuts app. However, the Shortcuts app doesn’t notify your app when these changes occur. It’s your app’s responsibility to keep its interface up to date with the latest shortcut changes.
> 앱에 표시되는 바로 가기를 업데이트합니다. 바로 가기 앱에서 사용자가 앱의 바로 가기를 추가, 제거 및 업데이트할 수 있습니다. 그러나 바로 가기 앱은 이러한 변경이 발생할 때 앱에 알리지 않습니다. 최신 바로 가기 변경사항으로 인터페이스를 최신 상태로 유지하는 것은 앱의 책임입니다.
>




# **Provide default phrases for shortcuts**
> 바로 가기에 대한 기본 구문 제공
>




Your app provides default phrases for shortcuts during setup. People can personalize these phrases when adding your shortcuts to Siri.
> 앱은 설치 중 바로 가기에 대한 기본 구문을 제공합니다. 사람들은 당신의 단축키를 시리에 추가할 때 이 문구들을 개인화할 수 있다.
>




**Keep phrases short and memorable.** Bear in mind that people must speak your phrase verbatim, so long or confusing phrases may result in mistakes and frustration. Two- and three-word phrases tend to work best. More words can be harder for people to remember, and phrases that are too long will get truncated.
> 문구를 짧고 기억에 남도록 하라. 사람들은 당신의 문구를 정확하게 말해야 한다. 그래서 길고 혼란스러운 문구는 실수와 좌절을 초래할 수 있다. 두 단어와 세 단어의 구절이 가장 효과적인 경향이 있다. 더 많은 단어들은 사람들이 기억하기 어려울 수 있고, 너무 긴 문구들은 잘릴 것이다.
>




**Make sure the phrases you suggest are accurate and specific.** Phrases like *Reorder coffee* or *Order my usual coffee* clearly describe what the shortcut does, which makes it easier for people to remember the phrase later. Also make sure that your suggested phrases are specific to each shortcut’s scope. For example, *Watch baseball* is clearer and more memorable than *Watch sports*. It’s also important to avoid implying that people can vary a shortcut’s invocation phrase to get a different result. For example, people might interpret a phrase like *Order a large clam chowder* to mean that your shortcut will give them what they want if they substitute “small” for “large” and “lobster bisque” for “clam chowder.”
> 제안하는 문구가 정확하고 구체적인지 확인하십시오. 커피 주문 또는 내 평소 커피 주문과 같은 문구는 단축키가 수행하는 작업을 명확하게 설명하므로 나중에 이 문구를 쉽게 기억할 수 있습니다. 또한 제안된 구문이 각 바로 가기의 범위에 적합한지 확인하십시오. 예를 들어, 워치 야구는 워치 스포츠보다 더 선명하고 기억에 남는다. 사람들이 다른 결과를 얻기 위해 단축키의 호출 구문을 변경할 수 있다는 암시를 피하는 것도 중요하다. 예를 들어, 사람들은 "작은 것"을 "큰 것"으로 대체하고 "랍스터 비스크"를 "클램 차우더"로 대체하면 당신의 지름길이 그들이 원하는 것을 줄 것이라는 의미로 큰 조개 차우더 주문과 같은 문구를 해석할 수 있다
>




