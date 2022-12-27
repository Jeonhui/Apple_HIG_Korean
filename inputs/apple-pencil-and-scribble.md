# **[inputs] apple-pencil-and-scribble**
## Apple Pencil helps make drawing, handwriting, and marking effortless and natural, in addition to performing well as a pointer and UI interaction tool.
> Apple Pencil은 포인터와 UI 상호 작용 도구로서 잘 수행될 뿐만 아니라 그리기, 필기 및 표시를 쉽고 자연스럽게 할 수 있도록 도와줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-apple-pencil-and-scribble-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-apple-pencil-and-scribble-intro_2x.png)

Apple Pencil is a versatile, intuitive tool for iPad apps that offers pixel‑level precision when jotting notes, sketching, painting, marking up documents, and more. Scribble lets people use Apple Pencil to enter text in any text field through fast, private, on-device handwriting recognition.
> Apple Pencil은 메모, 스케치, 그림 그리기, 문서 표시 등을 할 때 픽셀 수준의 정밀도를 제공하는 iPad 앱용 다목적 직관적 도구입니다. 스크라이블을 사용하면 Apple Pencil을 사용하여 장치에 있는 빠른 개인 필기 인식을 통해 텍스트 필드에 텍스트를 입력할 수 있습니다.
>




# **Best practices**

**Support behaviors people intuitively expect when using a marking instrument.** Most people have a lot of experience with real-world marking tools, and this knowledge informs their expectations when they use Apple Pencil with your app. To provide a delightful experience, think about the ways people interact with nondigital pencils, pens, and other marking instruments, and proactively support actions that people may naturally attempt. For example, people often want to write in the margins of documents or books.
> 사람들이 마킹 도구를 사용할 때 직관적으로 예상하는 행동을 지원합니다. 대부분의 사람들은 실제 마킹 도구에 대한 경험이 많으며, 이 지식은 그들이 당신의 앱과 함께 애플 펜슬을 사용할 때 그들의 기대를 알려줍니다. 즐거운 경험을 제공하기 위해, 사람들이 디지털 연필, 펜, 그리고 다른 표시 도구들과 상호 작용하는 방법에 대해 생각하고, 사람들이 자연스럽게 시도할 수 있는 행동들을 적극적으로 지원하세요. 예를 들어, 사람들은 종종 문서나 책의 여백에 글을 쓰고 싶어한다.
>




**Let people choose when to switch between Apple Pencil and finger input.** For example, if your app supports Apple Pencil for marking, also ensure that your app’s controls respond to Apple Pencil so people don’t have to switch to using their finger to activate them. In this scenario, a control that doesn’t support Apple Pencil input might seem to be unresponsive, giving the impression of a malfunction or low battery. (Scribble only supports Apple Pencil input.)
> Apple Pencil과 핑거 입력 사이에서 전환할 시기를 선택할 수 있습니다. 예를 들어, 앱이 표시를 위해 Apple Pencil을 지원하는 경우, 사용자가 손가락을 사용하여 활성화할 필요가 없도록 앱의 컨트롤이 Apple Pencil에 응답하는지 확인하십시오. 이 시나리오에서는 Apple Pencil 입력을 지원하지 않는 컨트롤이 응답하지 않는 것처럼 보여 배터리가 오작동하거나 부족한 것처럼 보일 수 있습니다. (스크립블은 Apple Pencil 입력만 지원합니다.)
>




**Let people make a mark the moment Apple Pencil touches the screen**. You want the experience of putting Apple Pencil to screen to mirror the experience of putting a classic pencil to paper, so it's essential to avoid requiring people to tap a button or enter a special mode before they can make a mark.
> 애플 펜슬이 화면에 닿는 순간 사람들이 표시를 하도록 하세요. 애플 펜슬을 화면에 띄워 클래식 펜슬을 종이에 갖다 대는 경험을 반영하고 싶으므로 표시를 하기 전에 버튼을 누르거나 특수 모드로 들어가는 것을 피하는 것이 중요합니다.
>




**Help people express themselves by responding to the way they use Apple Pencil.** Apple Pencil can sense tilt (altitude), force (pressure), and orientation (azimuth). Use this information to affect the strokes Apple Pencil makes, such as by varying thickness and intensity. When responding to pressure, keep things simple and intuitive. For example, it feels natural to affect continuous properties — such as ink opacity or brush size — by varying the pressure.
> 애플 펜슬은 기울기(고도), 힘(압력), 방향(방위)을 감지할 수 있다. 이 항목에서는 다양한 두께 및 강도 등으로 Apple Pencil의 획에 영향을 줄 수 있습니다. 압력에 대응할 때는 사물을 단순하고 직관적으로 유지하세요. 예를 들어, 압력을 변화시킴으로써 잉크 불투명도나 브러시 크기와 같은 연속적인 특성에 영향을 미치는 것은 당연한 것처럼 느껴진다.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/altitude.svg](https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/altitude.svg)

Altitude

![https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/pressure.svg](https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/pressure.svg)

Pressure

![https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/azimuth.svg](https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/azimuth.svg)

Azimuth

**Provide visual feedback to indicate a direct connection with content.** Make sure Apple Pencil appears to directly and immediately manipulate content it touches onscreen. Avoid letting Apple Pencil appear to initiate seemingly disconnected actions, or affect content on other parts of the screen.
> 콘텐츠와 직접 연결되어 있음을 나타내는 시각적 피드백을 제공합니다. Apple Pencil이 화면에서 직접 그리고 즉시 콘텐츠를 조작하는 것처럼 나타나는지 확인하십시오. Apple Pencil이 연결이 끊긴 것처럼 보이는 작업을 시작하거나 화면의 다른 부분의 콘텐츠에 영향을 주지 않도록 합니다.
>




**Design a great left- and right-handed experience.** Avoid placing controls in locations that may be obscured by either hand. If there’s a chance controls may become obscured, consider letting people reposition them.
> 훌륭한 왼손잡이와 오른손잡이 경험을 설계하십시오. 어느 한 손에 의해 가려질 수 있는 위치에 조정기를 배치하지 마십시오. 컨트롤이 모호해질 가능성이 있는 경우 사람들이 컨트롤의 위치를 변경하도록 허용하는 것을 고려하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/controls-moved-right.svg](https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/controls-moved-right.svg)

![https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/controls-moved-left.svg](https://developer.apple.com/design/human-interface-guidelines/inputs/apple-pencil-and-scribble/images/controls-moved-left.svg)

# **Hover**

With iPadOS 16 or later running on iPad Pro 11-inch (4th generation) or iPad Pro 12.9-inch (6th generation), the system can detect Apple Pencil (2nd generation) when it hovers up to 12 mm above the display.
> 아이패드 프로 11인치(4세대)나 아이패드 프로 12.9인치(6세대)에서 구동되는 아이패드 OS 16 이상에서는 디스플레이 위 12mm까지 맴돌면 애플 펜슬(2세대)을 감지할 수 있다.
>




**Use hover to help people predict what will happen when Apple Pencil touches the screen.**For example, as people hold Apple Pencil above the screen, a hover preview can show the dimensions and color of the mark that the current tool can make. As much as possible, avoid continuously modifying the preview as people move Apple Pencil closer or farther from the screen. A preview that changes according to height is unlikely to clarify the mark Apple Pencil will make, and frequent visual variations can be very distracting to people.
> 호버를 사용하면 Apple Pencil이 화면을 터치할 때 어떤 일이 일어날지 예측할 수 있습니다.예를 들어, 화면 위에 있는 Apple Pencil을 사용하면 마우스 미리 보기에서 현재 도구가 만들 수 있는 표시의 크기와 색상을 표시할 수 있습니다. 사용자가 화면에서 Apple Pencil을 이동할 때 미리 보기를 계속 수정하지 않도록 하십시오. 키에 따라 변하는 미리보기는 애플 펜슬이 어떤 표시를 할지 명확히 할 수 없을 것 같고, 잦은 시각적 변화는 사람들에게 매우 산만할 수 있다.
>




**Avoid using hover to initiate an action.** Unlike tapping a button or marking the screen, hovering is a relatively imprecise motion that doesn’t require people to think about the actual distance between Apple Pencil and the display. You don’t want people to inadvertently perform an action — especially a destructive action that they might want to undo — just because they hold Apple Pencil near the screen.
> 단추를 누르거나 화면을 표시하는 것과 달리 호버는 상대적으로 부정확한 동작이므로 Apple Pencil과 디스플레이 사이의 실제 거리를 고려할 필요가 없습니다. 사용자가 화면 근처에 Apple Pencil을 들고 있다는 이유만으로 작업(특히 실행 취소하려는 파괴적인 작업)을 실수로 수행하지 않도록 할 수 있습니다.
>




**Prefer showing a preview value that’s near the middle in a range of dynamic values.** Dynamic properties like opacity or flow can be difficult to depict at the highest or lowest ends of the spectrum. For example, previewing the appearance of a brush mark made with the maximum pressure could occlude the area in which people are marking; in contrast, depicting a mark made with the minimum pressure could be hard for people to detect, making the preview an inaccurate representation of an actual mark or even invisible.
> 동적 값 범위에서 중간에 가까운 미리보기 값을 표시하는 것을 선호합니다. 불투명도나 흐름과 같은 동적 특성은 스펙트럼의 가장 높은 쪽이나 가장 낮은 쪽에서 묘사하기 어려울 수 있습니다. 예를 들어, 최대 압력으로 만들어진 브러시 마크의 모양을 미리 보는 것은 사람들이 표시하는 영역을 포함할 수 있다; 반대로, 최소 압력으로 만든 마크를 묘사하는 것은 사람들이 감지하기 어려워서 미리보기가 실제 마크의 부정확한 표현이 되거나 심지어 보이지 않을 수도 있다.
>




**Consider using hover to enable relevant interactions close to where people are marking.** For example, you might use hover to display a contextual menu of tool sizes when people hold Apple Pencil above the screen and either double-tap it or press a modifier key on an attached keyboard. Revealing a menu near where people are marking lets them make choices without moving Apple Pencil or their hands to another part of the screen.
> 예를 들어 화면 위에서 Apple Pencil을 잡고 두 번 누르거나 연결된 키보드에서 수정자 키를 누를 때 호버를 사용하여 도구 크기의 상황에 맞는 메뉴를 표시할 수 있습니다. 표시하는 곳 근처에 메뉴를 표시하면 화면의 다른 부분으로 Apple Pencil이나 손을 이동하지 않고 선택할 수 있습니다.
>




**Prefer showing hover previews for Apple Pencil, not for a pointing device.** Although a pointing device can also respond to hover gestures, it might be confusing to provide the same visual feedback for both devices. If it makes sense in your app, you can restrict your hover preview to Apple Pencil only. For developer guidance, see [Adopting hover support for Apple Pencil](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/adopting_hover_support_for_apple_pencil).
> 포인팅 장치가 아닌 Apple Pencil의 호버 미리 보기를 표시하는 것을 선호합니다. 포인팅 장치가 호버 제스처에도 응답할 수 있지만 두 장치에 대해 동일한 시각적 피드백을 제공하는 것은 혼란스러울 수 있습니다. 앱에서 사용할 수 있는 경우 마우스 미리 보기를 Apple Pencil로만 제한할 수 있습니다. 개발자 지침은 Apple Pencil에 대한 호버 지원 채택을 참조하십시오.
>




# **Double tap**

**Respect people’s settings for the double-tap gesture when they make sense in your app.** By default, Apple Pencil (2nd generation) responds to the double-tap gesture by toggling between the current tool and the eraser, but people can set the gesture to toggle between the current and previous tool, show and hide the color picker, or do nothing at all. If your app supports these behaviors, let people use their preferred gestures to enable them. If the systemwide double-tap settings don’t make sense in your app, you can still use the gesture to change the mode of Apple Pencil (2nd generation). For example, a 3D app that offers a mesh-editing tool could use double-tap to toggle between the tool’s raise and lower modes.
> 기본적으로 Apple Pencil(2세대)은 현재 도구와 지우개를 전환하여 더블탭 제스처에 응답하지만, 사용자는 현재 도구와 이전 도구를 전환하거나 색 선택기를 표시하거나 숨기거나 아무 작업도 하지 않도록 제스처를 설정할 수 있습니다. 앱에서 이러한 동작을 지원하는 경우 사용자가 선호하는 제스처를 사용하여 동작을 활성화할 수 있습니다. 시스템 전체의 더블 탭 설정이 앱에서 의미가 없는 경우에도 제스처를 사용하여 Apple Pencil(2세대)의 모드를 변경할 수 있습니다. 예를 들어 메쉬 편집 도구를 제공하는 3D 앱은 더블 탭을 사용하여 도구의 상승 모드와 하강 모드를 전환할 수 있다.
>




**Give people a way to enable custom double-tap behavior if necessary.** If you offer custom double-tap behavior in addition to some or all of the default behaviors, provide a control that lets people choose the custom behavior mode. People need to know which mode they’re in; otherwise, they may get confused when your app responds differently to their interactions. In this scenario, make sure it’s easy for people to discover the custom behavior your app supports, but don’t enable it by default.
> 필요한 경우 사용자 지정 두 번 탭 동작을 사용할 수 있는 방법을 제공합니다. 기본 동작의 일부 또는 전부와 함께 사용자 지정 두 번 탭 동작을 제공하는 경우 사용자 지정 동작 모드를 선택할 수 있는 컨트롤을 제공합니다. 사람들은 그들이 어떤 모드에 있는지 알아야 한다; 그렇지 않으면, 그들은 당신의 앱이 그들의 상호작용에 다르게 반응할 때 혼란스러울 수 있다. 이 시나리오에서는 사용자가 앱에서 지원하는 사용자 지정 동작을 쉽게 검색할 수 있도록 하되 기본적으로 사용하지 않도록 설정합니다.
>




**Avoid using the double-tap gesture to perform an action that modifies content.** It’s possible for people to double-tap accidentally, which means that they may not even be aware that your app has performed the action. Prefer using double-tap to enable actions that are easy for people to undo. In particular, avoid using double-tap to perform a potentially destructive action that might result in data loss.
> 두 번 탭 제스처를 사용하여 콘텐츠를 수정하는 작업을 수행하지 마십시오. 사람들이 실수로 두 번 탭할 수 있습니다. 즉, 앱이 해당 작업을 수행했다는 사실조차 인식하지 못할 수 있습니다. 사용자가 실행 취소하기 쉬운 작업을 사용하려면 두 번 탭을 사용하는 것이 좋습니다. 특히 데이터 손실을 초래할 수 있는 잠재적으로 파괴적인 작업을 수행할 때는 두 번 탭을 사용하지 마십시오.
>




# **Scribble**

With Scribble and Apple Pencil, people can simply write wherever text is accepted in your app — they don’t have to tap or switch modes first. Because Scribble is fully integrated into iPadOS 14 and later, it’s available to all apps by default.
> Scribble과 Apple Pencil을 사용하면 앱에서 텍스트가 허용되는 곳에 쓰기만 하면 됩니다. 먼저 모드를 누르거나 전환할 필요가 없습니다. 스크라이브는 아이패드에 완전히 통합되어 있기 때문이다.OS 14 이상은 기본적으로 모든 앱에서 사용할 수 있습니다.
>




**Make text entry feel fluid and effortless.** By default, Scribble works in all standard text components — such as text fields, text views, search fields, and editable fields in web content — except password fields. If you use a custom text field in your app, avoid making people tap or select it before they can begin writing.
> 기본적으로 스크라이브는 암호 필드를 제외한 모든 표준 텍스트 구성요소(예: 텍스트 필드, 텍스트 보기, 검색 필드 및 웹 콘텐츠의 편집 가능한 필드)에서 작동합니다. 앱에서 사용자 지정 텍스트 필드를 사용하는 경우 쓰기를 시작하기 전에 먼저 사용자가 텍스트 필드를 누르거나 선택하지 않도록 합니다.
>




**Make Scribble available everywhere people might want to enter text.** Unlike using the keyboard, using Apple Pencil encourages people to treat the screen the way they treat a sheet of paper. Help strengthen this perception in your app by making Scribble consistently available in places where text entry seems natural. For example, in Reminders, it’s natural for people to create a new reminder by writing it in the blank space below the last item, even though the area doesn’t contain a text field. For developer guidance, see [UIIndirectScribbleInteraction](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction).
> 키보드를 사용하는 것과 달리 애플 펜슬을 사용하면 화면을 한 장의 종이를 처리하는 방식으로 처리할 수 있습니다. 텍스트 입력이 자연스러워 보이는 곳에서 스크라이브를 지속적으로 사용할 수 있도록 함으로써 앱에서 이러한 인식을 강화할 수 있습니다. 예를 들어, 알림에서 사용자는 영역에 텍스트 필드가 없더라도 마지막 항목 아래의 빈 공간에 알림을 작성하여 새 알림을 작성하는 것이 당연합니다. 개발자 지침은 UIIndirectScribble을 참조하십시오.상호작용.
>




**Avoid distracting people while they write.** Some text field behaviors work well for keyboard input, but can disrupt the natural writing experience that Apple Pencil enables. For example, it’s best to avoid displaying autocompletion text as people write in a text field because the suggestions can visually interfere with their writing. It’s also a good idea to hide a field’s placeholder text the moment people begin to write so that their input doesn’t appear to overlap it.
> 일부 텍스트 필드 동작은 키보드 입력에 적합하지만 Apple Pencil이 사용하는 자연스러운 쓰기 환경을 방해할 수 있습니다. 예를 들어, 제안이 시각적으로 작성을 방해할 수 있으므로 텍스트 필드에 사용자가 작성할 때 자동 완성 텍스트를 표시하지 않는 것이 좋습니다. 또한 사용자가 쓰기 시작하는 순간 필드의 자리 표시자 텍스트를 숨겨 입력 내용이 겹치지 않도록 하는 것도 좋습니다.
>




**While people are writing in a text field, make sure it remains stationary.** In some cases, it can make sense to move a text field when it becomes focused: for example, a search field might move to make more room to display results. Such a movement is fine when people are using the keyboard, but when they’re writing it can make them feel like they’ve lost control of where their input is going. If you can’t prevent a text field from moving or resizing, consider delaying the change until people pause their writing.
> 경우에 따라 검색 필드가 이동하여 결과를 표시할 공간을 늘릴 수 있으므로 텍스트 필드에 포커스가 있을 때 텍스트 필드를 이동하는 것이 좋습니다. 사람들이 키보드를 사용할 때는 이러한 움직임이 괜찮지만, 그들이 글을 쓸 때는 입력이 어디로 가는지를 통제하지 못하는 것처럼 느끼게 할 수 있다. 텍스트 필드의 이동 또는 크기 조정을 방지할 수 없는 경우, 사용자가 쓰기를 일시 중지할 때까지 변경을 연기하는 것이 좋습니다.
>




**Prevent autoscrolling text while people are writing and editing in a text field.** When transcribed text autoscrolls, people might try to avoid writing on top of it. Worse, if text scrolls while people are using Apple Pencil to select it, they might select a different range of text than they want.
> 텍스트 필드에서 사용자가 글을 쓰고 편집하는 동안 텍스트를 자동으로 스크롤하지 않도록 합니다. 텍스트를 자동으로 스크롤할 때 사용자는 텍스트 위에 글을 쓰는 것을 피하려고 할 수 있습니다. 더 나쁜 것은 사용자가 애플 펜슬을 사용하여 텍스트를 선택하는 동안 텍스트가 스크롤되면 사용자가 원하는 텍스트 범위가 다를 수 있습니다.
>




**Give people enough space to write.** A small text field can feel uncomfortable to write in. When you know that Apple Pencil input is likely, improve the writing experience in your app by increasing the size of the text field before people begin to write in it or when they pause writing; avoid resizing a text field while people are writing. For developer guidance, see [UIScribbleInteraction](https://developer.apple.com/documentation/uikit/uiscribbleinteraction).
> 사람들에게 쓰기에 충분한 공간을 제공하세요. 작은 텍스트 필드는 쓰기에 불편함을 느낄 수 있습니다. Apple Pencil이 입력될 가능성이 있는 경우, 사람들이 쓰기 시작하기 전에 또는 쓰기를 일시 중지할 때 텍스트 필드의 크기를 늘려 앱에서 쓰기 환경을 개선하십시오. 개발자 지침은 UIScrible을 참조하십시오.상호작용.
>




# **Custom drawing**

