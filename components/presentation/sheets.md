# **[components-presentation] sheets**

## A sheet helps people perform a scoped task that’s closely related to their current context.
> 시트는 사람들이 현재 컨텍스트와 밀접하게 관련된 범위가 지정된 작업을 수행하도록 도와줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/sheet-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/sheet-intro-dark_2x.png)

By default, a sheet is *modal*, presenting a focused experience that prevents people from interacting with the parent view until they dismiss the sheet (for more on modal presentation, see [Modality](../patterns/modality)). A modal sheet is useful for requesting specific information from people or enabling a simple task that they can complete before returning to the parent view. For example, a sheet might let people supply information needed to complete an action, such as attaching a file, choosing the location for a move or save, or specifying the format for a selection.
> 기본적으로 시트는 모달이며, 사람들이 시트를 해제할 때까지 부모 보기와 상호 작용하지 못하도록 하는 집중적인 환경을 제공합니다(모달 표시에 대한 자세한 내용은 모달 표시를 참조하십시오). 모달 시트는 사용자에게 특정 정보를 요청하거나 사용자가 상위 보기로 돌아가기 전에 완료할 수 있는 간단한 작업을 활성화하는 데 유용합니다. 예를 들어, 시트는 사용자가 파일 첨부, 이동 또는 저장 위치 선택 또는 선택 형식 지정과 같은 작업을 완료하는 데 필요한 정보를 제공하도록 할 수 있습니다.
>




In macOS and watchOS, a sheet is always modal, but in iOS and iPadOS, a sheet can also be nonmodal. When a nonmodal sheet is onscreen, people use its functionality to directly affect the current task in the parent view without dismissing the sheet. For example, Notes on iPhone and iPad uses a nonmodal sheet to help people apply different formatting to various text selections as they edit a note.
> 맥 OS와 워치 OS에서는 시트가 항상 모달이지만 iOS와 아이패드 OS에서는 시트가 비모달일 수도 있다. 비모달 시트가 화면에 나타나면 사용자는 시트를 해제하지 않고 부모 보기에서 현재 작업에 직접 영향을 미치기 위해 이 기능을 사용합니다. 예를 들어, iPhone 및 iPad의 Notes는 비모달 시트를 사용하여 사람들이 노트를 편집할 때 다양한 텍스트 선택에 다른 형식을 적용할 수 있도록 도와줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/nonmodal-sheet-ios-1-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/nonmodal-sheet-ios-1-dark_2x.png)

The Notes format sheet lets people apply formatting to selected text in the editing view.
> Notes 형식 시트를 사용하여 편집 보기에서 선택한 텍스트에 형식을 적용할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/nonmodal-sheet-ios-2-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/nonmodal-sheet-ios-2-dark_2x.png)

Because the sheet is nonmodal, people can make additional text selections without dismissing the sheet.
> 시트가 비모달이기 때문에, 사람들은 시트를 해제하지 않고 추가적인 텍스트 선택을 할 수 있다.
>




# **Best practices**

**Use a sheet to present nonimmersive content or enable simple tasks.** A sheet allows some of the parent view to remain visible, helping people retain their original context as they interact with the sheet.
> 시트를 사용하여 몰입형 콘텐츠를 표시하거나 간단한 작업을 수행할 수 있습니다. 시트를 사용하면 부모 보기 중 일부를 볼 수 있으므로 사용자가 시트와 상호 작용할 때 원래 컨텍스트를 유지할 수 있습니다.
>




**To present immersive content or enable complex tasks, consider alternatives to sheets.** For example, iOS and iPadOS offer a full-screen style of modal view that can work well to display immersive content — like videos, photos, or camera views — or multistep tasks like document or photo editing. (For developer guidance, see [UIModalPresentationStyle.fullScreen](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/fullscreen).) In a macOS experience, you might want to open a new window or let people enter full-screen mode instead of using a sheet. For example, a self-contained task like editing a document tends to work well in a separate window, whereas [full-screen mode](../patterns/going-full-screen) can help people view media or perform a more immersive task.
> iOS 및 iPadOS는 비디오, 사진 또는 카메라 뷰와 같은 몰입형 콘텐츠 또는 문서 또는 사진 편집과 같은 다단계 작업을 잘 표시할 수 있는 전체 화면 스타일의 모달 뷰를 제공합니다(개발자 지침은 UIModalPresentationStylef 참조).ullScreen.) MacOS 환경에서는 시트를 사용하는 대신 새 창을 열거나 전체 화면 모드로 전환할 수 있습니다. 예를 들어 문서 편집과 같은 자체 포함된 작업은 별도의 창에서 잘 작동하는 경향이 있는 반면 전체 화면 모드는 사람들이 미디어를 보거나 더 몰입적인 작업을 수행하는 데 도움이 될 수 있다.
>




**Display only one sheet at a time from the main interface.** When people close a sheet, they expect to return to the parent view or window. If closing a sheet takes people back to another sheet, they can lose track of where they are in your app. If something people do within a sheet results in another sheet appearing, close the first sheet before displaying the new one. If necessary, you can display the first sheet again after people dismiss the second one.
> 기본 인터페이스에서 한 번에 하나의 시트만 표시합니다. 사람들이 시트를 닫을 때, 그들은 부모 보기나 창으로 돌아갈 것으로 예상합니다. 시트를 닫으면 사용자가 다른 시트로 돌아가면 앱에서 자신이 어디에 있는지 모를 수 있습니다. 사용자가 시트 내에서 수행한 작업으로 인해 다른 시트가 나타나는 경우 새 시트를 표시하기 전에 첫 번째 시트를 닫으십시오. 필요한 경우, 사람들이 두 번째 시트를 해제한 후 첫 번째 시트를 다시 표시할 수 있습니다.
>




**Use a nonmodal view when you want to present supplementary items that affect the main task in the parent view.** In macOS, you can use a [panel](../components/presentation/panels) to give people access to information and actions they need while continuing to interact with the main window; in iOS and iPadOS, you can use a nonmodal sheet to enable this workflow. For guidance, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets#ios-ipados).
> 부모 보기에서 주 작업에 영향을 미치는 보충 항목을 표시하려면 비모달 보기를 사용하십시오. macOS에서는 패널을 사용하여 사람들이 기본 창과 계속 상호 작용하면서 필요한 정보와 작업에 액세스할 수 있도록 할 수 있습니다. iOS 및 iPadOS에서는 비모달 시트를 사용하여 이 워크플로우를 활성화할 수 있습니다. 자세한 내용은 iOS, iPadOS를 참조하십시오.
>




# **Platform considerations**

*No additional considerations for tvOS.*

# **iOS, iPadOS**

A resizable sheet expands when people scroll its contents or drag the *grabber*, which is a small horizontal indicator that can appear at the top edge of a sheet. Sheets resize according to their *detents*, which are particular heights at which a sheet naturally rests. Designed for iPhone, detents specify particular heights at which a sheet naturally rests. The system defines two detents: *large* is the height of a fully expanded sheet and *medium* is about half of the fully expanded height.
> 크기 조정 가능한 시트는 사용자가 내용을 스크롤하거나 그라버를 끌면 확장됩니다. 그라버는 시트의 상단 가장자리에 나타날 수 있는 작은 수평 표시기입니다. 시트는 시트가 자연스럽게 놓여 있는 특정 높이인 멈춤쇠에 따라 크기가 조정됩니다. iPhone용으로 설계된 멈춤쇠는 시트가 자연스럽게 놓이는 특정 높이를 지정합니다. 이 시스템은 두 개의 멈춤쇠를 정의합니다. 큰 것은 완전히 확장된 시트의 높이이고 중간 것은 완전히 확장된 높이의 약 절반입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/large-detent-area-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/large-detent-area-dark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/medium-detent-area-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/medium-detent-area-dark_2x.png)

Sheets automatically support the large detent. Adding the medium detent allows the sheet to rest at both heights, whereas specifying only medium prevents the sheet from expanding to full height. For developer guidance, see [detents](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/3801903-detents).
> 시트는 자동으로 큰 멈춤쇠를 지지합니다. 중간 멈춤쇠를 추가하면 시트가 두 높이 모두에서 고정되는 반면, 중간만 지정하면 시트가 전체 높이로 확장되지 않습니다. 개발자 지침은 멈춤쇠를 참조하십시오.
>




**In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet’s content.** For example, a share sheet displays the most relevant items within the medium detent, where they’re visible without resizing. To view more items, people can scroll or expand the sheet. In contrast, you might not want to support the medium detent if a sheet’s content is more useful when it displays at full height. For example, the compose sheets in Messages and Mail display only at full height to give people enough room to create content.
> iPhone 앱에서는 시트의 내용을 점진적으로 공개할 수 있도록 미디어 멈춤쇠를 지원합니다. 예를 들어, 쉐어 시트는 미디어 멈춤쇠 내에서 크기 조정 없이 볼 수 있는 가장 관련성이 높은 항목을 표시합니다. 더 많은 항목을 보기 위해 사용자는 시트를 스크롤하거나 확장할 수 있습니다. 반대로, 시트의 내용이 최대 높이로 표시될 때 더 유용한 경우에는 중간 멈춤쇠를 지원하지 않을 수 있습니다. 예를 들어, 메시지 및 메일의 작성 시트는 사용자가 내용을 작성할 수 있는 충분한 공간을 제공하기 위해 최대 높이에서만 표시됩니다.
>




**Include a grabber in a resizable sheet.** A grabber shows people that they can drag the sheet to resize it; they can also tap it to cycle through the detents. In addition to providing a visual indicator of resizability, a grabber also works with VoiceOver so people can resize the sheet without seeing the screen. For developer guidance, see [prefersGrabberVisible](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/3801906-prefersgrabbervisible).
> 크기를 조정할 수 있는 시트에 그라버를 포함합니다. 그라버는 사용자가 시트를 끌어 크기를 조정할 수 있으며, 멈춤쇠를 눌러 시트를 순환시킬 수도 있음을 보여줍니다. 화면 크기를 시각적으로 표시하는 것 외에도, 그라버는 보이스오버와 함께 작동하여 사람들이 화면을 보지 않고도 시트 크기를 조정할 수 있습니다. 개발자 지침은 grabberVisible 기본 설정을 참조하십시오.
>




**Support swiping to dismiss a sheet.** People expect to swipe vertically to dismiss a sheet instead of tapping a dismiss button. If people have unsaved changes in the sheet when they begin swiping to dismiss it, use an action sheet to let them confirm their action.
> 시트를 제거하기 위해 스와이프하는 것을 지원합니다. 사람들은 해제 버튼을 누르는 대신 시트를 제거하기 위해 수직으로 스와이프하는 것을 기대합니다. 사용자가 시트를 삭제하기 위해 스와이프를 시작할 때 저장되지 않은 변경사항이 있는 경우, 수행 시트를 사용하여 작업을 확인할 수 있습니다.
>




**Position Done and Cancel buttons as people expect.** Typically, a Done or Dismiss button belongs in a sheet’s top-right corner (in a left-to-right layout) or top-left corner (in a right-to-left layout). The Cancel button belongs in a sheet’s top-left (in a left-to-right layout) or top-right (in a right-to-left layout) corner.
> 일반적으로 완료 또는 취소 단추는 시트의 오른쪽 상단 모서리(왼쪽에서 오른쪽으로 레이아웃) 또는 왼쪽 상단 모서리(오른쪽에서 왼쪽으로 레이아웃)에 있습니다. Cancel(취소) 버튼은 시트의 왼쪽 상단(왼쪽에서 오른쪽으로 레이아웃) 또는 오른쪽 상단(오른쪽에서 왼쪽으로 레이아웃) 모서리에 있습니다.
>




# **macOS**

In macOS, a sheet is a cardlike view with rounded corners that floats on top of its parent window. The parent window is dimmed while the sheet is onscreen, signaling that people can’t interact with it until they dismiss the sheet. However, people expect to interact with other app windows before dismissing a sheet.
> macOS에서 시트(sheet)는 둥근 모서리가 있는 카드 모양의 뷰로, 상위 창 위에 뜬다. 시트가 화면에 있는 동안에는 상위 창이 흐리게 표시되어 시트를 제거할 때까지 사용자가 해당 창과 상호 작용할 수 없음을 나타냅니다. 그러나 사람들은 시트를 파기하기 전에 다른 앱 창과 상호 작용하기를 기대한다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/sheets-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/sheets-macos_2x.png)

**Present a sheet in a reasonable default size.** People don’t generally expect to resize sheets, so it’s important to use a size that’s appropriate for the content you display. In some cases, however, people appreciate a resizable sheet — such as when they need to expand the contents for a clearer view — so it’s a good idea to support resizing.
> 사람들은 일반적으로 시트 크기를 조정하지 않으므로 표시하는 내용에 적합한 크기를 사용하는 것이 중요합니다. 그러나 더 선명한 보기를 위해 콘텐츠를 확장해야 하는 경우와 같이 크기 조정 가능한 시트를 높이 평가하는 경우도 있으므로 크기 조정을 지원하는 것이 좋습니다.
>




**Let people interact with other app windows without first dismissing a sheet.** When a sheet opens, you bring its parent window to the front — if the parent window is a document window, you also bring forward its modeless document-related panels. When people want to interact with other windows in your app, make sure they can bring those windows forward even if they haven’t dismissed the sheet yet.
> 사용자가 먼저 시트를 제거하지 않고 다른 앱 창과 상호 작용할 수 있도록 합니다. 시트가 열리면 상위 창이 앞쪽으로 이동합니다. 상위 창이 문서 창인 경우에는 모델이 없는 문서 관련 패널도 앞으로 이동합니다. 사람들이 당신의 앱에서 다른 창과 상호 작용하기를 원할 때, 그들이 아직 시트를 치우지 않았더라도 그 창들을 앞으로 가져올 수 있는지 확인하세요.
>




**Position a sheet’s dismiss buttons as people expect.** People expect to find all buttons that dismiss a sheet — including Done, OK, and Cancel — at the bottom of the view, in the trailing corner.
> 사람들은 보기 하단의 뒤쪽 모서리에서 완료, 확인 및 취소를 포함하여 시트의 해제 단추를 모두 찾을 수 있습니다.
>




**Use a panel instead of a sheet if people need to repeatedly provide input and observe results.** A find and replace panel, for example, might let people initiate replacements individually, so they can observe the result of each search for correctness. For guidance, see [Panels](../components/presentation/panels).
> 사람들이 반복적으로 입력을 제공하고 결과를 관찰해야 하는 경우에는 시트 대신 패널을 사용하십시오. 예를 들어, 패널 찾기 및 교체를 통해 사람들이 개별적으로 교체 작업을 시작하여 정확성을 확인할 수 있습니다. 자세한 내용은 패널을 참조하십시오.
>




# **watchOS**

In watchOS, a sheet is a full-screen view that slides over your app’s current screen.
> watchOS에서 시트는 앱의 현재 화면 위로 미끄러지는 전체 화면 보기입니다.
>




**Use a sheet only when your modal task requires a custom title or custom content presentation.** In contrast, if you need to give people important information or enable choices, use an [alert](../components/presentation/alerts) or [action sheet](../components/presentation/action-sheets).
> 모달 작업에 사용자 지정 제목 또는 사용자 지정 내용 프레젠테이션이 필요한 경우에만 시트를 사용하십시오. 반대로, 다른 사용자에게 중요한 정보를 제공하거나 선택 사항을 사용하려면 경고 또는 수행 시트를 사용하십시오.
>




**Keep sheet interactions brief and occasional.** Use custom sheets only as a temporary interruption to the current workflow, and use them only to facilitate an important task. Avoid using a sheet to help people navigate your app’s content.
> 사용자 지정 시트는 현재 워크플로우에 대한 일시적인 중단으로만 사용하고 중요한 작업을 수행할 때만 사용하십시오. 사용자가 앱의 콘텐츠를 탐색하는 데 도움이 되는 시트를 사용하지 마십시오.
>




**Change the default label of the dismiss control only if doing so makes sense in your app.** By default, the system displays Cancel in the top-leading corner of the sheet. Use Cancel when the sheet lets people make changes to the app’s behavior or to their data. On the other hand, if your sheet simply presents information without enabling a task, use Done or Dismiss because people don’t need a way to cancel changes they might have made. Regardless of the label you choose, the system always displays the text in white.
> 앱에서 실행하는 것이 타당한 경우에만 해제 컨트롤의 기본 레이블을 변경하십시오. 기본적으로 시스템은 시트의 맨 위에 있는 모서리에 취소를 표시합니다. 사용자가 앱의 동작이나 데이터를 변경할 수 있는 경우 취소를 사용합니다. 반면, 시트가 작업을 사용 가능으로 설정하지 않고 정보만 표시하는 경우에는 사용자가 변경한 내용을 취소할 필요가 없으므로 완료 또는 해제를 사용하십시오. 선택한 레이블에 관계없이 시스템은 항상 텍스트를 흰색으로 표시합니다.
>




**If you change the default label, avoid confusing alternatives.** Avoid using a label that might mislead people into thinking that the sheet is part of a hierarchical navigation interface. Also, if the text in the top-leading corner looks like a page or app title — or if you don’t provide a button label — people won’t know how to dismiss the sheet.
> 기본 레이블을 변경할 경우 다른 레이블을 혼동하지 않도록 하십시오. 레이블을 사용하면 사람들이 시트가 계층 탐색 인터페이스의 일부라고 오해할 수 있습니다. 또한 맨 위에 있는 텍스트가 페이지 또는 앱 제목처럼 보이거나 단추 레이블을 제공하지 않으면 사람들은 시트를 제거하는 방법을 알 수 없습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/modal-sheet-watchos-do_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/modal-sheet-watchos-do_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/modal-sheet-watchos-do-not-1_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/modal-sheet-watchos-do-not-1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/modal-sheet-watchos-do-not-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/sheets/images/modal-sheet-watchos-do-not-2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)
