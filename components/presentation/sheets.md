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

