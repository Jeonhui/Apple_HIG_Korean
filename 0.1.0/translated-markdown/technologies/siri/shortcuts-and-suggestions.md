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




**Don’t commandeer core Siri commands.** For example, your app should never suggest a phrase like *Call 911* or include the text *Hey Siri*.
> 핵심 Siri 명령을 강요하지 마십시오. 예를 들어, 앱은 Call 911과 같은 문구를 제안하거나 Hey Siri 텍스트를 포함해서는 안 됩니다.
>




# **Make shortcuts customizable**

When you define a parameter for each detail your app needs to perform an intent, people can customize the shortcut by editing these details in the Shortcuts app or your Add to Siri sheet.
> 앱에서 의도를 수행하는 데 필요한 각 세부 정보에 대한 매개 변수를 정의하면 바로 가기 앱 또는 시리에 추가 시트에서 이러한 세부 정보를 편집하여 바로 가기를 사용자 지정할 수 있습니다.
>




To show people which details they can edit and how their edits affect the action, you provide a *parameter summary*. A parameter summary succinctly describes the action by using the parameters in a sentence that begins with a verb. For example, a customizable *Order coffee* shortcut could display a parameter summary like “Order *quantity* *coffee*” where *quantity* and *coffee* are the parameters that people can edit. Here’s an example of how the *Order coffee* shortcut might look after people supply values for the *quantity* and *coffee* parameters.
> 사용자가 편집할 수 있는 세부사항과 편집한 내용이 수행에 미치는 영향을 사용자에게 표시하려면 매개변수 요약을 제공합니다. 매개 변수 요약은 동사로 시작하는 문장의 매개 변수를 사용하여 동작을 간결하게 설명합니다. 예를 들어, 사용자 정의 가능한 커피 주문 바로 가기는 "커피 주문 수량"과 같은 매개 변수 요약을 표시할 수 있습니다. 여기서 수량과 커피는 사용자가 편집할 수 있는 매개 변수입니다. 다음은 커피 주문 바로 가기가 사람들이 수량 및 커피 매개변수에 대한 값을 제공한 후 어떻게 보이는지 보여주는 예입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/edited-parameter-summary_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/edited-parameter-summary_2x.png)

**Provide a parameter summary for each custom intent you support.** At minimum, your parameter summary should include all parameters your intent requires and any parameters that receive values from other apps or actions. The summary doesn’t have to include optional parameters or parameters that people aren’t likely to edit; if you omit parameters like these from the summary, people can still access them in the Show More section.
> 지원하는 각 사용자 지정 의도에 대한 매개 변수 요약을 제공하십시오. 최소한 매개 변수 요약에는 해당 의도에 필요한 모든 매개 변수와 다른 앱 또는 작업에서 값을 받는 모든 매개 변수가 포함되어야 합니다. 요약에는 사용자가 편집하지 않는 선택적 매개 변수나 매개 변수가 포함될 필요가 없습니다. 요약에서 이러한 매개 변수를 생략해도 사용자는 추가 표시 섹션에서 해당 매개 변수에 액세스할 수 있습니다.
>




**Craft a short parameter summary that’s clearly related to your intent’s title.** When the intent title and the parameter summary are similar, it’s easy for people to recognize the action regardless of where they view it. Aim to use the same words in the summary and the title — in particular, it’s helpful to begin both phrases with the same verb. For example, if your intent title is “Search encyclopedia”, a good parameter summary could be “Search encyclopedia for *search term*”.
> 의도 제목과 명확하게 관련된 짧은 매개 변수 요약을 작성합니다. 의도 제목과 매개 변수 요약이 유사할 때, 사람들은 그들이 어디에서 보든 간에 행동을 쉽게 인식할 수 있습니다. 요약과 제목에서 동일한 단어를 사용하는 것을 목표로 합니다. 특히 두 구문 모두 동일한 동사로 시작하는 것이 도움이 됩니다. 예를 들어, 원하는 제목이 "백과사전 검색"인 경우, 좋은 매개변수 요약은 "검색어에 대한 백과사전 검색"이 될 수 있습니다.
>




**Aim for a parameter summary that reads like a sentence.** Use sentence-style capitalization, but don’t include ending punctuation. When possible, avoid punctuation entirely. Punctuation within a summary — especially colons, semicolons, and parentheses — can make the summary hard to read and understand.
> 문장처럼 읽는 매개 변수 요약을 목표로 합니다. 문장 형식의 대소문자를 사용하되, 구두점 끝은 포함하지 마십시오. 가능한 경우 구두점을 완전히 사용하지 마십시오. 요약 내 구두점(특히 콜론, 세미콜론 및 괄호)은 요약을 읽고 이해하기 어려울 수 있습니다.
>




**Provide multiple parameter summaries when necessary.** If your action includes a parameter that has a parent-child relationship with other parameters, you can provide multiple variants of the summary based on the current value of the parent parameter. For example, if your *order coffee*shortcut lets people specify whether they want to pick up their order or have it delivered, your parameter summary should reflect the current choice. In this scenario, you should create one parameter summary that helps people pick a store location and another summary that helps them pick a delivery address. Be sure to use a consistent grammatical structure and parameter order in all variants of the summary that you create.
> 필요한 경우 여러 개의 매개 변수 요약을 제공하십시오. 작업에 다른 매개 변수와 상위-하위 관계가 있는 매개 변수가 포함된 경우 상위 매개 변수의 현재 값을 기준으로 여러 변형의 요약을 제공할 수 있습니다. 예를 들어, 주문 커피 바로 가기를 통해 사람들이 주문을 수령할지 배달할지 지정할 수 있는 경우, 매개 변수 요약은 현재 선택 사항을 반영해야 합니다. 이 시나리오에서는 사용자가 상점 위치를 선택하는 데 도움이 되는 하나의 매개 변수 요약과 배달 주소를 선택하는 데 도움이 되는 다른 요약을 생성해야 합니다. 작성하는 요약의 모든 변형에서 일관된 문법 구조와 매개 변수 순서를 사용해야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/parent-parameter-choice_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/parent-parameter-choice_2x.png)

Delivery or pickup

![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/child-parameter-choice_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/child-parameter-choice_2x.png)

Delivery location

**Provide output parameters for information that people can use in a multistep shortcut.** For example, an *order coffee* action might provide output that includes the estimated delivery time and the cost of the order. With this information, people could create a multistep shortcut that messages a friend about the delivery time and logs the transaction in their favorite budgeting app.
> 사람들이 다단계 단축키로 사용할 수 있는 정보에 대한 출력 매개변수를 제공합니다. 예를 들어, 주문 커피 작업은 예상 배송 시간과 주문 비용을 포함하는 출력을 제공할 수 있습니다. 이 정보로, 사람들은 친구에게 배달 시간에 대해 메시지를 보내고 그들이 가장 좋아하는 예산 책정 앱에 거래를 기록하는 다단계 바로 가기를 만들 수 있다.
>




**Consider defining an input parameter.** When you define an input parameter for an action, the action can automatically receive output from a preceding action in a multistep shortcut. For example, if your action applies a filter to the image it receives in an *image* parameter, you might designate *image* as the input parameter so that it automatically accepts images from other actions. You configure an input parameter in your intent definition file (shown in “Define User-Configurable Shortcuts” in [Adding user interactivity with Siri shortcuts and the Shortcuts app](https://developer.apple.com/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app)).
> 입력 매개 변수를 정의하는 것을 고려해 보십시오. 작업에 대한 입력 매개 변수를 정의할 때 작업은 이전 작업의 출력을 다단계 바로 가기에서 자동으로 수신할 수 있습니다. 예를 들어, 작업이 이미지 매개 변수에서 수신하는 이미지에 필터를 적용하는 경우 다른 작업의 이미지를 자동으로 받아들이도록 이미지를 입력 매개 변수로 지정할 수 있습니다. 사용자 정의 파일에서 입력 매개 변수를 구성합니다("사용자 구성 가능한 바로 가기 정의"의 "Siri 바로 가기 및 바로 가기 앱을 사용하여 사용자 상호 작용 추가"에 표시됨).
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/input-output-parameters_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/input-output-parameters_2x.png)

**Help people distinguish among different variations of the same action.** For example, an app that offers a *send message* action might use a contact photo to help people visually distinguish the various messages they send. To do this, choose the parameter that’s most identifiable to people and designate it as the key parameter (shown in “Define User-Configurable Shortcuts” in [Adding user interactivity with Siri shortcuts and the Shortcuts app](https://developer.apple.com/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app)). Be sure to provide an image for the key parameter every time you donate the action (for developer guidance, see [INImage](https://developer.apple.com/documentation/sirikit/inimage)).
> 예를 들어, 메시지 보내기 동작을 제공하는 앱은 연락처 사진을 사용하여 사람들이 보내는 다양한 메시지를 시각적으로 구분할 수 있습니다. 이렇게 하려면 사용자가 가장 쉽게 식별할 수 있는 매개변수를 선택하고 키 매개변수로 지정합니다("사용자 구성 가능한 바로 가기 정의"의 "Siri 바로 가기 및 바로 가기 앱 사용자 상호작용 추가"에 표시됨). 작업을 기부할 때마다 키 매개 변수에 대한 이미지를 제공해야 합니다(개발자 지침은 INImage 참조).
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/multiple-intent-configurations_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/multiple-intent-configurations_2x.png)

**Avoid providing multiple actions that perform the same basic task.** For example, instead of providing an action that adds text to a note and a different action that adds an image, consider providing a single action that lets people add both types of content. Providing a few high-level actions can make it easier for people to understand what the actions do when they’re combined in a multistep shortcut.
> 노트에 텍스트를 추가하는 작업과 이미지를 추가하는 다른 작업을 제공하는 대신 두 가지 유형의 콘텐츠를 모두 추가할 수 있는 단일 작업을 제공하는 것이 좋습니다. 몇 가지 높은 수준의 작업을 제공하면 사용자가 여러 단계의 바로 가기에서 작업을 결합할 때 수행하는 작업을 쉽게 이해할 수 있습니다.
>




For developer guidance, see [Shortcut management](https://developer.apple.com/documentation/sirikit/shortcut_management).

# **Add to Siri button styles**
> Siri 버튼 스타일에 추가
>




The Add to Siri button is available in several visual styles. You can also customize the corner radius of the buttons to match your app’s interface.
> Add to Siri 버튼은 여러 가지 시각적 스타일로 사용할 수 있습니다. 또한 앱의 인터페이스에 맞게 버튼의 모서리 반지름을 사용자 지정할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black_2x.png)

**Black.** Use on white or light-color backgrounds that provide sufficient contrast. Don’t use on black or dark backgrounds.
> 검은색. 흰색 또는 밝은 색 배경에 사용하여 충분한 대비를 제공합니다. 검은색이나 어두운 배경에는 사용하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black-Outlined_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-Black-Outlined_2x.png)

**Black with outline.** Use on dark backgrounds that provide sufficient contrast. Don’t use on white or light-color backgrounds.
> 윤곽이 있는 검은색. 대비가 충분히 되는 어두운 배경에 사용합니다. 흰색이나 밝은 색 배경에는 사용하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White_2x.png)

**White.** Use on dark backgrounds that provide sufficient contrast. Don’t use on white or light-color backgrounds.
> 흰색. 대비가 충분한 어두운 배경에 사용합니다. 흰색이나 밝은 색 배경에는 사용하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White-Outlined_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-White-Outlined_2x.png)

**White with outline.** Use on white or light-color backgrounds that don’t provide sufficient contrast. Don’t use on dark or saturated backgrounds.
> 윤곽선이 있는 흰색. 대비가 충분하지 않은 흰색 또는 밝은 색 배경에 사용합니다. 어둡거나 포화된 배경에는 사용하지 마십시오.
>




**Accommodate the variable width of the Add to Siri button.** The width of the button varies in different locales and when updated to display the user’s invocation phrase.
> Add to Siri 버튼의 가변 너비를 수용합니다. 버튼의 너비는 사용자의 호출 구문을 표시하도록 업데이트할 때와 로케일마다 다릅니다.
>




**Maintain clear space around the Add to Siri button.** At minimum, leave padding of 1/10 the button’s height on all sides of the button.
> Add to Siri 버튼 주변에 공백을 유지하고 버튼 높이의 1/10 이상의 패딩을 버튼의 모든 면에 남겨둡니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-ClearSpace_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/AddToSiri-ClearSpace_2x.png)

# **Display multiple shortcuts in one place**
> 한 곳에 여러 바로 가기 표시
>




If your app contains more than a few shortcuts, consider creating a dedicated area of the app to display them. A dedicated screen makes it easy for people to see all of your app’s shortcuts at a glance and to add the shortcuts they want to use. Alternatively, consider offering follow-up questions to support additional options for a single shortcut.
> 앱에 몇 개 이상의 바로 가기가 포함되어 있는 경우 앱의 전용 영역을 만들어 바로 가기를 표시하는 것을 고려해 보십시오. 전용 화면을 사용하면 사용자가 앱의 모든 바로 가기를 한 눈에 쉽게 볼 수 있고 사용할 바로 가기를 추가할 수 있습니다. 또는 단일 바로 가기에 대한 추가 옵션을 지원하는 후속 질문을 제공하는 것을 고려해 보십시오.
>




**Use an unambiguous title for your list of shortcuts.** For example, using “Siri Shortcuts” for the navigation bar title clearly communicates the purpose of the screen.
> 바로 가기 목록에는 명확한 제목을 사용하십시오. 예를 들어, 탐색 모음 제목에 "Siri 바로 가기"를 사용하면 화면의 목적을 명확하게 알 수 있습니다.
>




**Consider creating a custom Add button for a list of shortcuts.** The system-provided Add to Siri button can add too much visual weight when it’s used several times in one view. If the screen makes it clear that all the items in the list are Siri Shortcuts, you can display a simpler button that uses “Add” or “+” for each shortcut in the list.
> 시스템에서 제공하는 Add to Siri 버튼은 한 뷰에서 여러 번 사용할 경우 시각적인 무게를 너무 많이 추가할 수 있습니다. 화면에서 목록의 모든 항목이 Siri 바로 가기임을 분명히 표시하면 목록의 각 바로 가기에 대해 "추가" 또는 "+"를 사용하는 더 간단한 단추를 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-list-shortcuts-added_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/add-to-siri-list-shortcuts-added_2x.png)

**Provide feedback when a shortcut has been added.** Show people that they’ve successfully added a shortcut by replacing the Add button with an Edit button and displaying the phrase they recorded. Alternatively, you can remove the Add button and let people tap the phrase they recorded to open an editing view.
> 바로 가기가 추가되었을 때 피드백을 제공합니다. 추가 단추를 편집 단추로 바꾸고 사용자가 기록한 구문을 표시하여 바로 가기를 성공적으로 추가했음을 사람들에게 보여줍니다. 또는 추가 단추를 제거하고 사용자가 기록한 구문을 눌러 편집 보기를 열 수 있습니다.
>



