# **[components-menus-and-actions] activity-views**

## An activity view — often called a *share sheet* — presents a range of tasks that people can perform in the current context.
> 작업 보기(종종 공유 시트라고 함)는 현재 컨텍스트에서 사용자가 수행할 수 있는 작업 범위를 나타냅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/activity-view-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/activity-view-intro-dark_2x.png)

Activity views present sharing activities like messaging and actions like Copy and Print, in addition to quick access to frequently used apps. People typically reveal a share sheet by choosing an Action button while viewing a page or document, or after they’ve selected an item. An activity view can appear as a sheet or a popover, depending on the device and orientation.
> 활동 보기는 자주 사용하는 앱에 대한 빠른 액세스뿐만 아니라 복사 및 인쇄와 같은 메시지 및 작업과 같은 공유 활동을 표시합니다. 일반적으로 페이지 또는 문서를 보는 동안 또는 항목을 선택한 후 수행 단추를 선택하여 공유 시트를 표시합니다. 활동 보기는 장치 및 방향에 따라 시트 또는 팝업으로 나타날 수 있습니다.
>




You can provide app-specific activities that can appear in a share sheet when people open it within your app or game. For example, Photos provides app-specific actions like Copy Photo, Add to Album, and Adjust Location. By default, the system lists app-specific actions before actions — such as Add to Files or AirPlay — that are available in multiple apps or throughout the system. People can edit the list of actions to ensure that it displays the ones they use most and to add new ones.
> 앱 또는 게임 내에서 다른 사람이 공유 시트를 열 때 해당 시트에 나타날 수 있는 앱별 활동을 제공할 수 있습니다. 예를 들어, 사진은 사진 복사, 앨범에 추가, 위치 조정과 같은 앱별 작업을 제공합니다. 기본적으로 시스템은 여러 앱에서 또는 시스템 전체에서 사용할 수 있는 작업(예: 파일에 추가 또는 AirPlay) 전에 앱별 작업을 나열합니다. 작업 목록을 편집하여 가장 많이 사용하는 작업 목록을 표시하고 새 작업 목록을 추가할 수 있습니다.
>




You can also create app extensions to provide custom share and action activities that people can use in other apps. (An *app extension* is code you provide that people can install and use outside of your app.) For example, you might create a custom share activity that people can install to help them share a webpage with a specific social media service. Even though macOS doesn’t provide an activity view, you can create share and action app extensions that people can use on a Mac. For guidance, see [Share and action extensions](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/activity-views#share-and-action-extensions).
> 또한 앱 확장을 만들어 다른 앱에서 사용할 수 있는 사용자 지정 공유 및 작업 활동을 제공할 수 있습니다. (앱 확장은 앱 외부에서 설치하고 사용할 수 있는 코드입니다.) 예를 들어 사용자가 특정 소셜 미디어 서비스와 웹 페이지를 공유할 수 있도록 설치할 수 있는 사용자 지정 공유 활동을 만들 수 있습니다. MacOS가 활동 보기를 제공하지 않더라도 Mac에서 사용할 수 있는 공유 및 작업 앱 확장을 만들 수 있습니다. 자세한 내용은 공유 및 작업 확장을 참조하십시오.
>




# **Best practices**

**Avoid creating duplicate versions of common actions that are already available in the activity view.** For example, providing a duplicate Print action is unnecessary and confusing because people wouldn’t know how to distinguish your action from the system-provided one. If you need to provide app-specific functionality that’s similar to an existing action, give it a custom title. For example, if you enable custom formatting to print a bank transaction, use a title that helps people understand what your print activity does, like “Print Transaction.”
> 작업 보기에서 이미 사용 가능한 일반 작업의 중복 버전을 만들지 마십시오. 예를 들어, 중복 인쇄 작업을 제공하는 것은 불필요하고 혼란스럽습니다. 다른 사람이 사용자의 작업을 시스템에서 제공한 작업과 구별하는 방법을 모르기 때문입니다. 기존 작업과 유사한 앱별 기능을 제공해야 하는 경우 사용자 지정 제목을 지정하십시오. 예를 들어, 은행 트랜잭션을 인쇄하기 위해 사용자 정의 서식을 사용 가능으로 설정하는 경우, "트랜잭션 인쇄"와 같이 인쇄 활동이 수행하는 작업을 다른 사람이 이해할 수 있도록 도와주는 제목을 사용하십시오.
>




**Consider using a symbol to represent your custom activity.** [SF Symbols](../foundations/sf-symbols)provides a comprehensive set of configurable symbols you can use to communicate items and concepts in an activity view. If you need to create a custom interface icon, center it in an area measuring about 70x70 pixels. For guidance, see [Icons](../foundations/icons).
> 사용자 지정 활동을 나타내는 기호를 사용해 보십시오. SF 기호는 활동 보기에서 항목과 개념을 전달하는 데 사용할 수 있는 구성 가능한 포괄적인 기호 집합을 제공합니다. 사용자 지정 인터페이스 아이콘을 만들어야 하는 경우 약 70x70 픽셀 크기의 영역에 아이콘을 가운데에 놓습니다. 자세한 내용은 아이콘을 참조하십시오.
>




**Write a succinct, descriptive title for each custom action you provide.** If a title is too long, the system wraps it and may truncate it. Prefer a single verb or a brief verb phrase that clearly communicates what the action does. Avoid including your company or product name in an action title. In contrast, the share sheet displays the title of a share activity — typically a company name — below the icon that represents it.
> 제공하는 각 사용자 지정 작업에 대해 간결하고 설명적인 제목을 작성합니다. 제목이 너무 길면 시스템이 해당 제목을 감아서 잘라낼 수 있습니다. 동작이 무엇을 하는지 명확하게 전달하는 단일 동사 또는 간단한 동사 구문을 선호합니다. 작업 제목에 회사 또는 제품 이름을 포함하지 않도록 합니다. 대조적으로, 공유 시트는 공유 활동의 제목(일반적으로 회사 이름)을 나타내는 아이콘 아래에 표시합니다.
>




**Make sure activities are appropriate for the current context.** Although you can’t reorder system-provided tasks in an activity view, you can exclude tasks that aren’t applicable to your app. For example, if it doesn’t make sense to print from within your app, you can exclude the Print activity. You can also identify which custom tasks to show at any given time.
> 액티비티가 현재 컨텍스트에 적합한지 확인하십시오. 액티비티 보기에서 시스템에서 제공한 작업의 순서를 변경할 수는 없지만 앱에 적용되지 않는 작업은 제외할 수 있습니다. 예를 들어 앱 내에서 인쇄할 수 없는 경우 인쇄 작업을 제외할 수 있습니다. 또한 언제든지 표시할 사용자 정의 태스크를 식별할 수 있습니다.
>




**Use the Share button to display an activity view.** People are accustomed to accessing system-provided activities when they choose the Share button. Avoid confusing people by providing an alternative way to do the same thing.
> Share(공유) 버튼을 사용하여 활동 보기를 표시합니다. Share(공유) 버튼을 선택하면 시스템에서 제공하는 활동에 액세스하는 데 익숙합니다. 같은 일을 할 수 있는 대안적인 방법을 제공함으로써 사람들을 혼란스럽게 하는 것을 피하세요.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/activity-views/images/share-button_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/activity-views/images/share-button_2x.png)

# **Share and action extensions**

Share extensions give people a convenient way to share information from the current context with apps, social media accounts, and other services. Action extensions let people initiate content-specific tasks — like adding a bookmark, copying a link, editing an inline image, or displaying selected text in another language — without leaving the current context.
> 공유 확장을 통해 사람들은 앱, 소셜 미디어 계정 및 기타 서비스와 현재 컨텍스트의 정보를 편리하게 공유할 수 있습니다. 작업 확장을 사용하면 현재 컨텍스트를 벗어나지 않고 책갈피 추가, 링크 복사, 인라인 이미지 편집 또는 다른 언어로 선택한 텍스트 표시와 같은 내용별 태스크를 시작할 수 있습니다.
>




The system presents share and action extensions differently depending on the platform:
> 시스템은 플랫폼에 따라 공유 및 작업 확장을 다르게 제공합니다.
>




- In iOS and iPadOS, share and action extensions are displayed in the share sheet that appears when people choose an Action button.
- >  iOS 및 iPad OS에서 공유 및 작업 확장 기능은 사용자가 작업 단추를 선택할 때 나타나는 공유 시트에 표시됩니다.

- In macOS, people access share extensions by clicking a Share button in the toolbar or choosing Share in a context menu. People can access an action extension by holding the pointer over certain types of embedded content — like an image they add to a Mail compose window — clicking a toolbar button, or choosing a quick action in a Finder window.
- >  macOS에서 사람들은 도구 모음에서 공유 단추를 클릭하거나 상황에 맞는 메뉴에서 공유를 선택하여 공유 확장에 액세스합니다. 사용자는 메일 작성 창에 추가하는 이미지와 같은 특정 유형의 내장된 콘텐츠 위에 포인터를 놓고 도구 모음 단추를 클릭하거나 파인더 창에서 빠른 수행을 선택하여 수행 확장에 액세스할 수 있습니다.


**If necessary, create a custom interface that feels familiar to people.** For a share extension, prefer the system-provided composition view because it provides a consistent sharing experience that people already know. For an action extension, include your app name. If you need to present an interface, include elements of your app’s interface to help people understand that your extension and your app are related.
> 필요한 경우 사용자에게 친숙한 사용자 지정 인터페이스를 만듭니다. 공유 확장의 경우 시스템에서 제공하는 구성 보기를 선호합니다. 사용자가 이미 알고 있는 일관된 공유 환경을 제공하기 때문입니다. 작업 확장의 경우 앱 이름을 포함합니다. 인터페이스를 제공해야 하는 경우 앱 인터페이스의 요소를 포함하면 확장자와 앱이 관련이 있다는 것을 사람들이 이해할 수 있습니다.
>




**Streamline and limit interaction.** People appreciate extensions that let them perform a task in just a few steps. For example, a share extension might immediately post an image to a social media account with a single tap or click.
> 상호 작용을 간소화하고 제한합니다. 사람들은 몇 단계만으로 작업을 수행할 수 있는 확장 기능을 높이 평가합니다. 예를 들어 공유 확장 기능은 한 번의 탭 또는 클릭으로 이미지를 즉시 소셜 미디어 계정에 게시할 수 있습니다.
>




**Avoid placing a modal view above your extension.** By default, the system displays an extension within a modal view. While it might be necessary to display an alert above an extension, avoid displaying additional modal views.
> 확장명 위에 모달 보기를 배치하지 마십시오. 기본적으로 시스템은 모달 보기 내에 확장명을 표시합니다. 확장자 위에 알림을 표시해야 할 수도 있지만 추가 모달 보기는 표시하지 않도록 합니다.
>




**If necessary, provide an image that communicates the purpose of your extension.** A share extension automatically uses your app icon, helping give people confidence that your app provided the extension. For an action extension, prefer using a [symbol](../foundations/sf-symbols) or creating an interface [icon](../foundations/icons) that clearly identifies the task.
> 필요한 경우 확장의 목적을 전달하는 이미지를 제공합니다. 공유 확장 기능은 자동으로 앱 아이콘을 사용하여 사용자에게 확장 기능을 제공했다는 확신을 심어줍니다. 작업 확장의 경우 작업을 명확하게 식별하는 인터페이스 아이콘이나 기호를 사용하는 것을 선호합니다.
>




**Use your main app to denote the progress of a lengthy operation.** An activity view dismisses immediately after people complete the task in your share or action extension. If a task is time-consuming, continue it in the background, and give people a way to check the status in your main app. Although you can use a notification to tell people about a problem, don’t notify them simply because the task completes.
> 기본 앱을 사용하여 긴 작업의 진행률을 표시합니다. 작업 보기는 공유 또는 작업 확장에서 작업을 완료하면 즉시 해제됩니다. 작업이 시간이 많이 걸리는 경우 백그라운드에서 작업을 계속하고 사람들에게 기본 앱의 상태를 확인할 수 있는 방법을 제공합니다. 통지를 사용하여 사용자에게 문제에 대해 알릴 수 있지만, 작업이 완료되었다고 해서 사용자에게 알리지 마십시오.
>




# **Platform considerations**

*No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, or watchOS.*
> iOS 또는 iPad OS에 대한 추가 고려 사항 없음. macOS, tvOS 또는 watch에서 지원되지 않음OS.
>



