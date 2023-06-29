# **[technologies] photo-editing**

# Photo-editing extensions let people modify photos and videos within the Photos app by applying filters or making other changes.
> 사진 편집 확장 기능을 사용하면 사람들이 필터를 적용하거나 다른 내용을 변경하여 사진 및 비디오를 수정할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-photo-editing-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-photo-editing-intro_2x.png)

Edits are always saved in the Photos app as new files, safely preserving the original versions.
> 편집한 내용은 항상 새 파일로 사진 앱에 저장되므로 원본을 안전하게 보존할 수 있습니다.
>




To access a photo editing extension, a photo must be in edit mode. While in edit mode, tapping the extension icon in the toolbar displays an action menu of available editing extensions. Selecting one displays the extension’s interface in a modal view containing a navigation bar. Dismissing this view confirms and saves the edit, or cancels it and returns to the Photos app.
> 사진 편집 확장에 액세스하려면 사진이 편집 모드에 있어야 합니다. 편집 모드에 있는 동안 도구 모음에서 확장 아이콘을 누르면 사용 가능한 편집 확장의 작업 메뉴가 표시됩니다. 하나를 선택하면 탐색 모음이 포함된 모달 보기에서 확장의 인터페이스가 표시됩니다. 이 보기를 취소하면 편집 내용을 확인하고 저장하거나, 편집 내용을 취소하고 사진 앱으로 돌아갑니다.
>




# **Best practices**

**Confirm cancellation of edits.** Editing a photo or video can be time consuming. If someone taps the Cancel button, don’t immediately discard their changes. Ask them to confirm that they really want to cancel, and inform them that any edits will be lost after cancellation. There’s no need to show this confirmation if no edits have been made yet.
> 편집 취소를 확인합니다. 사진이나 비디오를 편집하는 데 시간이 걸릴 수 있습니다. 다른 사용자가 취소 단추를 누른 경우 변경 내용을 즉시 취소하지 마십시오. 취소할 것인지 확인하고 취소 후 편집 내용이 손실된다는 사실을 알려달라고 요청합니다. 아직 편집하지 않은 경우에는 이 확인을 표시할 필요가 없습니다.
>




**Don’t provide a custom navigation bar.** Your extension loads within a modal view that already includes a navigation bar. Providing a second navigation bar is confusing and takes space away from the content being edited.
> 사용자 지정 탐색 모음을 제공하지 마십시오. 탐색 모음이 이미 포함된 모달 보기 내에서 확장이 로드됩니다. 두 번째 탐색 모음을 제공하는 것은 혼란스럽고 편집 중인 내용에서 공간을 빼앗습니다.
>




**Let people preview edits.** It’s hard to approve an edit if you can’t see what it looks like. Let people see the result of their work before closing your extension and returning to the Photos app.
> 편집 내용을 미리 볼 수 없습니다. 편집 내용을 확인할 수 없으면 편집을 승인하기 어렵습니다. 내선 번호를 닫고 사진 앱으로 돌아가기 전에 사람들이 작업 결과를 볼 수 있도록 합니다.
>




**Use your app icon for your photo editing extension icon.** This instills confidence that the extension is in fact provided by your app.
> 앱 아이콘을 사용하여 사진 편집 확장 아이콘을 사용하십시오. 이 아이콘은 앱이 확장을 제공한다는 확신을 심어줍니다.
>



