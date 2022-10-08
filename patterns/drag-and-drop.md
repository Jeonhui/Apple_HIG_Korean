# **[patterns] drag-and-drop**

# Using drag and drop, people can move or duplicate selected photos, text, and other content by dragging the selection from one location to another.
> 드래그 앤 드롭을 사용하여 선택한 사진, 텍스트 및 기타 콘텐츠를 한 위치에서 다른 위치로 끌어서 이동하거나 복제할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-drag-and-drop-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-drag-and-drop-intro-dark_2x.png)

iOS, iPadOS, and macOS support drag and drop through gestures on the touchscreen, interactions with a pointing device, and through full keyboard-access mode. In addition, Universal Control lets people drag content between their Mac and iPad. On a Mac, drag and drop is also available to VoiceOver users.
> iOS, iPadOS 및 macOS는 터치 스크린의 제스처, 포인팅 장치와의 상호 작용 및 전체 키보드 액세스 모드를 통해 드래그 앤 드롭을 지원합니다. 게다가, 유니버설 컨트롤은 사람들이 맥과 아이패드 사이에서 콘텐츠를 끌 수 있게 해준다. Mac에서는 VoiceOver 사용자가 드래그 앤 드롭을 사용할 수도 있습니다.
>




To perform drag and drop, people select content in one location, called the *source*, and drop it in another, called the *destination*. These locations can be in the same container — like a text view — or in different containers, like text views on opposite sides of a split view, or even in different apps.
> 끌어서 놓기를 수행하기 위해 사람들은 소스라고 하는 한 위치에서 콘텐츠를 선택하고 대상이라고 하는 다른 위치에 놓습니다. 이러한 위치는 텍스트 보기와 같이 동일한 컨테이너에 있을 수도 있고, 분할 보기의 반대편에 있는 텍스트 보기와 같이 다른 컨테이너에 있을 수도 있고, 다른 앱에 있을 수도 있습니다.
>




Depending on various factors, the drag and drop action might *move* the selected content to the destination or *copy* it. After a successful drop, moved content exists only in the destination; copied content exists in both locations. As a general rule, dropping selected content within the same container moves it, whereas dropping content in a different container copies it. Dragging and dropping content between apps always results in a copy.
> 다양한 요인에 따라 끌어서 놓기 작업이 선택한 내용을 대상으로 이동하거나 복사할 수 있습니다. 성공적으로 삭제하면 이동된 콘텐츠는 대상에만 존재하며 복사된 콘텐츠는 두 위치 모두에 존재합니다. 일반적으로, 선택한 내용을 같은 컨테이너 내에 삭제하면 이동하지만, 다른 컨테이너에 삭제하면 내용이 복사됩니다. 앱 간에 콘텐츠를 끌어다 놓으면 항상 복사본이 생성됩니다.
>




# **Best practices**

**As much as possible, support drag and drop throughout your app.** Most people are familiar with drag and drop and they often try it everywhere. When you use system-provided components — such as text fields and text views — you get built-in support for drag and drop.
> 가능한 한 앱 전체에서 드래그 앤 드롭을 지원합니다. 대부분의 사람들은 드래그 앤 드롭에 익숙하고 그들은 종종 어디에서나 그것을 시도한다. 텍스트 필드 및 텍스트 보기와 같은 시스템에서 제공하는 구성요소를 사용하면 드래그 앤 드롭에 대한 기본 제공 지원을 받을 수 있습니다.
>




**Offer alternative ways to accomplish drag-and-drop actions.** Sometimes, drag-and-drop operations are inconvenient or impossible for people to perform, so it’s important to provide other ways to do the same things. For example, you can include menu commands that people can use to copy an item and move it to another location. In iOS and iPadOS, you can use accessibility APIs to identify sources and destinations so that people can use assistive technologies to drag and drop in your app (for developer guidance, see [accessibilityDragSourceDescriptors](https://developer.apple.com/documentation/objectivec/nsobject/2891001-accessibilitydragsourcedescripto) and [accessibilityDropPointDescriptors](https://developer.apple.com/documentation/objectivec/nsobject/2891048-accessibilitydroppointdescriptor)).
> 끌어서 놓기 작업을 수행할 수 있는 다른 방법을 제공합니다. 드래그 앤 드롭 작업은 때때로 사람들이 수행하기에 불편하거나 불가능하므로 동일한 작업을 수행할 수 있는 다른 방법을 제공하는 것이 중요합니다. 예를 들어, 사용자가 항목을 복사하고 다른 위치로 이동하는 데 사용할 수 있는 메뉴 명령을 포함할 수 있습니다. iOS 및 iPadOS에서 접근성 API를 사용하여 소스 및 대상을 식별할 수 있으므로 보조 기술을 사용하여 앱을 끌어다 놓을 수 있습니다(개발자 지침은 접근성 DragSourceDescriptors 및 접근성 DropPointDescriptors 참조).
>




**Determine when dragging and dropping content within your app should result in a move or a copy.** In general, a move makes sense when the source and destination containers are the same — such as dragging text from one location to another within a document — and a copy makes sense when they’re different, like dragging an image from one document to another. Before you change these defaults, consider the behavior that most people expect and prefer the one that is least likely to result in frustration or data loss.
> 앱 내에서 콘텐츠를 끌어서 놓으면 이동 또는 복사가 발생하는 시기를 결정합니다. 일반적으로 원본 컨테이너와 대상 컨테이너가 동일한 경우(예: 문서 내 한 위치에서 다른 위치로 텍스트 끌기) 이동은 의미가 있으며, 복사본은 서로 다른 경우(예: 한 문서에서 다른 문서로 이미지 끌기) 의미가 있습니다. 이러한 기본값을 변경하기 전에 대부분의 사용자가 예상하는 동작과 데이터 손실로 이어질 가능성이 가장 낮은 동작을 고려해야 합니다.
>




**Support multi-item drag and drop when it makes sense.** People appreciate the convenience of dragging a group of items to a destination, instead of dragging each item separately. In iOS, iPadOS, and macOS, people can select multiple items and drag them as a group; in iPadOS, people can select an item, start dragging it, and add other items to the group without stopping the drag operation.
> 다중 항목 끌어서 놓기를 지원합니다. 사람들은 각 항목을 개별적으로 끄는 대신 한 그룹의 항목을 대상으로 끌 수 있는 편리함을 높이 평가합니다. iOS, iPadOS, macOS에서는 여러 항목을 선택하여 그룹으로 끌 수 있으며, iPadOS에서는 끌기 작업을 멈추지 않고 항목을 선택하고 끌기를 시작하여 그룹에 다른 항목을 추가할 수 있습니다.
>




**Prefer letting people undo a drag-and-drop operation.** Sometimes, people inadvertently drop content in the wrong destination, so they appreciate being able to undo the action and return to their previous state. You might also be able to help people avoid mistakes by asking for confirmation before completing a drag-and-drop operation that can’t be undone. In macOS, for example, the Finder asks for confirmation when people drag a file into a write-only folder because they won’t be able to open the folder and remove the dropped item. In some situations, it might make sense to provide a way to reverse the results of drag and drop when people can’t undo it. For example, Photos lets people cancel photo sharing after dropping a photo into a shared photo stream.
> 끌어서 놓기 작업을 실행 취소하도록 허용하십시오. 때때로, 사람들은 잘못된 목적지에 실수로 콘텐츠를 떨어뜨리기 때문에, 그들은 그 행동을 취소하고 이전 상태로 돌아갈 수 있다는 것에 감사한다. 또한 취소할 수 없는 끌어서 놓기 작업을 완료하기 전에 확인을 요청하여 실수를 방지할 수 있습니다. 예를 들어 macOS에서 파인더는 폴더를 열고 삭제된 항목을 제거할 수 없기 때문에 사용자가 파일을 쓰기 전용 폴더로 끌 때 확인을 요청합니다. 경우에 따라 드래그 앤 드롭의 결과를 되돌릴 수 없을 때 뒤집을 수 있는 방법을 제공하는 것이 합리적일 수 있습니다. 예를 들어, 사진을 공유 사진 스트림에 떨어뜨린 후 사진 공유를 취소할 수 있습니다.
>




**Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity.** By providing multiple alternatives, the destination can choose the highest quality version it can accept. For example, if people can drag a line drawing they created in your app, you could offer a PDF vector representation, a lossless PNG image with transparency, and a lossy JPEG image without transparency, in that order. Another example is an app that uses rich, complicated objects, like charts. This app might offer the native chart object followed by a simpler version — like an image of the chart — for destinations that don’t support chart objects.
> 가장 높은 충실도에서 가장 낮은 충실도로 정렬된 여러 버전의 드래그 콘텐츠를 제공하는 것을 고려해 보십시오. 여러 대안을 제공함으로써, 목적지는 받아들일 수 있는 최고 품질의 버전을 선택할 수 있다. 예를 들어, 만약 사람들이 당신의 앱에서 만든 선 그림을 끌 수 있다면, 당신은 PDF 벡터 표현, 투명도가 있는 무손실 PNG 이미지, 투명도가 없는 무손실 JPEG 이미지를 순서대로 제공할 수 있다. 또 다른 예는 차트처럼 풍부하고 복잡한 객체를 사용하는 앱이다. 이 앱은 차트 개체를 지원하지 않는 대상에 대해 네이티브 차트 개체와 차트 이미지와 같은 간단한 버전을 제공할 수 있습니다.
>




**Consider enabling spring loading.** Spring loading lets people activate certain controls, like buttons and segmented controls, by dragging selected content over them. For example, Calendar lets people drag a selected event over the day, week, month, or year segments in the toolbar, giving them a convenient way to move the event to a different date. On a Mac equipped with a Magic Trackpad, a button or segmented control can activate when people force-click it while continuing to hold the content; on iPad, these components can activate when people hover over them while holding the content.
> 스프링 로드를 활성화하는 것을 고려하십시오. 스프링 로드를 사용하면 선택한 콘텐츠를 해당 컨트롤 위로 끌어 버튼 및 세그먼트 컨트롤과 같은 특정 컨트롤을 활성화할 수 있습니다. 예를 들어, 달력을 사용하면 선택한 이벤트를 도구 모음의 일, 주, 월 또는 연도 세그먼트에 걸쳐 끌 수 있으므로 이벤트를 다른 날짜로 편리하게 이동할 수 있습니다. Magic Trackpad가 장착된 Mac에서는 사용자가 콘텐츠를 계속 누르고 있을 때 버튼이나 세그먼트화된 컨트롤이 활성화될 수 있으며 iPad에서는 이러한 구성 요소가 콘텐츠를 잡고 있을 때 사용자가 해당 구성 요소 위로 마우스를 가져가면 활성화될 수 있습니다.
>




# **Providing feedback**

Drag and drop is a dynamic process that can result in multiple outcomes. To help people feel in control the process, it’s crucial to provide clear and continuous feedback throughout.
> 끌어서 놓기는 여러 결과를 초래할 수 있는 동적 프로세스입니다. 사람들이 그 과정을 통제한다고 느낄 수 있도록 하기 위해서는, 명확하고 지속적인 피드백을 제공하는 것이 중요하다.
>




**Display a drag image as soon as people drag a selection about three points.** It works well to create a translucent representation of the content people are dragging. Translucency helps distinguish the representation from the original content and lets people see destinations as they pass over them. Display the drag image until people drop the content.
> 선택 영역을 약 세 점으로 끌면 바로 끌기 이미지를 표시합니다. 사람들이 끌고 있는 콘텐츠를 반투명하게 표현하는 것이 효과적이다. 반투명성은 표현과 원래의 내용을 구별하는 데 도움이 되고 사람들이 목적지를 지나갈 때 목적지를 볼 수 있게 한다. 사용자가 내용을 삭제할 때까지 드래그 이미지를 표시합니다.
>




**If it adds clarity, modify the drag image to help people predict the result of a drag-and-drop operation.** For example, when dragging a photo into a document, the drag image could expand to show the default size of the photo in the document. You can also use drag *flocking* to visually group multiple drag items — letting people confirm that they haven’t missed an item they want to drag — and then ungroup the items when people drop them. Although changing the drag image can provide valuable feedback, avoid creating a distracting experience in which the drag image is constantly and radically changing.
> 선명도가 더해진다면 드래그 이미지를 수정하여 드래그 앤 드롭 작업의 결과를 예측할 수 있습니다. 예를 들어 사진을 문서로 끌 때 끌기 이미지가 확장되어 문서에 있는 사진의 기본 크기를 표시할 수 있습니다. 끌기 모음을 사용하여 여러 끌기 항목을 시각적으로 그룹화하여 끌려는 항목을 놓치지 않았는지 확인한 다음 사용자가 항목을 놓을 때 해당 항목의 그룹화를 해제할 수도 있습니다. 드래그 이미지를 변경하면 귀중한 피드백을 제공할 수 있지만 드래그 이미지가 지속적으로 급격하게 변경되는 산만한 환경을 만들지 않도록 합니다.
>




**Show people whether a destination can accept dragged content.** For example, you might display an insertion point or highlight a containing view only when the destination can accept a dragged item, and show no visual feedback — or an explicit “not allowed” image, like the `circle.slash` SF symbol — when it can’t. Display highlighting or other visual cues only while the content is positioned above the destination, removing the visual feedback when people drag the content away. When there are multiple possible destinations, provide visual cues that help people identify one at a time.
> 대상이 끌어온 콘텐츠를 허용할 수 있는지 여부를 사용자에게 표시합니다. 예를 들어, 대상이 끌어온 항목을 수락할 수 있고 시각적 피드백('circle'과 같은 명시적 "허용되지 않은" 이미지)을 표시할 수 있는 경우에만 삽입 지점을 표시하거나 포함 보기를 강조 표시할 수 있습니다.슬래시의 SF 기호 - 할 수 없는 경우. 콘텐츠가 대상 위에 있는 동안만 강조 표시 또는 기타 시각적 신호를 표시하여 사용자가 콘텐츠를 끌 때 시각적 피드백을 제거합니다. 가능한 목적지가 여러 개 있는 경우, 사람들이 한 번에 하나씩 식별하는 데 도움이 되는 시각적 단서를 제공합니다.
>




**When people drop an item on an invalid destination, or when dropping fails, provide visual feedback.** For example, the item can move back from its current location to its source (if the source is still visible) or it can scale up and fade out to give the impression of the item evaporating instead of landing successfully.
> 사람들이 잘못된 대상에 항목을 떨어뜨리거나 떨어뜨리는 데 실패할 경우 시각적 피드백을 제공합니다. 예를 들어, 항목이 현재 위치에서 해당 소스로 다시 이동하거나(출처가 여전히 보이는 경우) 성공적으로 착륙하는 대신 항목이 증발하는 듯한 인상을 주기 위해 스케일업 및 페이드아웃할 수 있습니다.
>




# **Accepting drops**

**Scroll the contents of a destination when necessary.** When people drag an item within a scrolling container that has a lot of content, the content can automatically scroll as people move the item over it. This behavior makes it easy for people to find the right place to drop the item, but if they continue the drag operation outside of the container, automatic scrolling is no longer necessary. System-provided text views and text fields behave this way by default.
> 필요한 경우 대상의 내용을 스크롤합니다. 콘텐츠가 많은 스크롤 컨테이너 내에서 사용자가 항목을 끌면 해당 항목 위로 이동할 때 내용이 자동으로 스크롤될 수 있습니다. 이 동작을 통해 사람들은 물건을 떨어뜨릴 적절한 장소를 쉽게 찾을 수 있지만, 용기 밖에서 끌기 작업을 계속하면 더 이상 자동 스크롤이 필요하지 않습니다. 시스템에서 제공한 텍스트 보기 및 텍스트 필드는 기본적으로 이러한 방식으로 작동합니다.
>




**When there’s a choice, pick the richest version of dropped content your app can accept.** For example, if people drag a chart object from another app, the drag operation might offer both the rich, native chart object and a simple image of it. If your app supports charts, extract and display the native chart object; it it doesn’t, use the image instead.
> 선택할 수 있는 경우, 앱이 허용할 수 있는 가장 풍부한 삭제 콘텐츠 버전을 선택하십시오. 예를 들어, 다른 앱에서 차트 개체를 끌어다 놓으면 드래그 작업이 리치 네이티브 차트 개체와 해당 개체의 간단한 이미지를 모두 제공할 수 있습니다. 앱이 차트를 지원하는 경우 네이티브 차트 개체를 추출하고 표시하지만 그렇지 않으면 이미지를 대신 사용하십시오.
>




