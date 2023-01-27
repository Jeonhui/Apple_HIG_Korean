# **[technologies] icloud**

# iCloud is a service that lets people seamlessly access the content they care about—photos, videos, documents, and more—from any device, without performing explicit synchronization.
> iCloud는 명시적 동기화를 수행하지 않고도 사용자가 원하는 컨텐츠(사진, 비디오, 문서 등)에 모든 장치에서 원활하게 액세스할 수 있도록 해주는 서비스입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-iCloud-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-iCloud-intro_2x.png)

A fundamental aspect of iCloud is transparency. People don’t need to know where content resides. They can just assume they’re always accessing the latest version.
> 아이클라우드의 근본적인 측면은 투명성이다. 사람들은 콘텐츠가 어디에 있는지 알 필요가 없다. 그들은 항상 최신 버전에 액세스하고 있다고 가정할 수 있습니다.
>




**Make it easy to use your app with iCloud.** People enable iCloud in Settings and expect apps to work with it automatically. If you think people might want to choose whether to use iCloud with your app, show a simple option the first time your app opens that provides a choice between using iCloud for all data or not at all.
> iCloud로 앱을 쉽게 사용할 수 있습니다. 사람들은 설정에서 iCloud를 활성화하고 앱이 자동으로 작동하기를 기대합니다. 사람들이 당신의 앱과 함께 iCloud를 사용할지 여부를 선택하고 싶을 것이라고 생각한다면, 앱이 처음 열렸을 때 모든 데이터에 대해 iCloud를 사용할지 여부를 선택할 수 있는 간단한 옵션을 보여주십시오.
>




**Avoid asking which documents to keep in iCloud.** Most people expect all of their content to be available in iCloud and don’t want to manage the storage of individual documents. Consider how your app handles and exposes content, and try to perform more file-management tasks automatically.
> iCloud에 보관할 문서를 묻는 것을 피하십시오. 대부분의 사용자는 자신의 모든 컨텐츠를 iCloud에서 사용할 수 있기를 기대하며 개별 문서의 스토리지를 관리하고 싶어하지 않습니다. 앱이 콘텐츠를 처리하고 노출하는 방식을 고려하고 더 많은 파일 관리 작업을 자동으로 수행합니다.
>




**Keep content up to date when possible.** In iCloud-enabled apps, its best when people always have access to the most recent content. However, you need to balance this experience with respect to device storage and bandwidth constraints. If your app works with very large documents, it may be better to let people control when updated content is downloaded. If your app fits in this category, design a way to indicate that a more recent version of a document is available in iCloud. When a document is updating, provide subtle feedback if the download takes more than a few seconds.
> 가능하면 콘텐츠를 최신 상태로 유지하십시오. 아이클라우드 지원 앱에서는 사람들이 항상 최신 콘텐츠에 액세스할 수 있을 때 가장 좋습니다. 그러나 장치 저장 및 대역폭 제약 조건과 관련하여 이러한 경험의 균형을 유지해야 합니다. 앱이 매우 큰 문서에서 작동하는 경우 업데이트된 콘텐츠가 다운로드될 때 사람들이 제어할 수 있도록 하는 것이 더 나을 수 있습니다. 앱이 이 범주에 해당하는 경우 iCloud에서 최신 버전의 문서를 사용할 수 있음을 나타내는 방법을 설계하십시오. 문서를 업데이트할 때 다운로드가 몇 초 이상 걸릴 경우 미묘한 피드백을 제공합니다.
>




**Respect iCloud storage space.** iCloud is a finite resource for which people pay. Use iCloud to store information people create and understand, and avoid using it for app resources or content you can regenerate. Even if your app doesn’t implement iCloud support, remember that iCloud backups include the contents of every app’s Documents folder. To avoid using up too much space, be picky about the content you place in the Documents folder.
> iCloud 스토리지 공간을 존중합니다. iCloud는 사람들이 비용을 지불하는 유한한 자원입니다. iCloud를 사용하여 사람들이 만들고 이해하는 정보를 저장하고 재생성할 수 있는 앱 리소스나 콘텐츠에 사용하지 않도록 합니다. 앱이 iCloud 지원을 구현하지 않더라도, iCloud 백업에는 모든 앱의 Documents 폴더의 내용이 포함됩니다. 공간을 너무 많이 사용하지 않으려면 문서 폴더에 있는 내용을 선택해야 합니다.
>




**Make sure your app behaves appropriately when iCloud is unavailable.** If someone manually disables iCloud or turns on Airplane Mode, you don’t need to display an alert notifying them the iCloud is unavailable. They already know this. However, it may still be helpful to unobtrusively let them know that changes they make won’t be available on other devices until iCloud access is restored.
> iCloud를 사용할 수 없을 때 앱이 제대로 작동하는지 확인하십시오. 수동으로 iCloud를 사용하지 않도록 설정하거나 비행기 모드를 설정한 경우에는 iCloud를 사용할 수 없음을 알리는 경고를 표시할 필요가 없습니다. 그들은 이미 이것을 알고 있다. 그러나 iCloud 액세스가 복원될 때까지 다른 장치에서 변경 내용을 사용할 수 없다는 것을 사용자에게 알리는 것이 여전히 도움이 될 수 있습니다.
>




**Keep app state information in iCloud.** In addition to storing documents and other files, you can use iCloud to store settings and information about the state of your app. For example, a magazine app might store the last page viewed so when the app is opened on another device, someone can continue reading from where they left off. If you use iCloud to store settings, make sure it’s for ones people want applied to all of their devices. For example, some settings might be more useful at work than at home.
> 앱 상태 정보를 iCloud에 보관합니다. 문서 및 기타 파일을 저장하는 것 외에도 iCloud를 사용하여 앱 상태에 대한 설정 및 정보를 저장할 수 있습니다. 예를 들어, 잡지 앱은 마지막으로 본 페이지를 저장하여 다른 장치에서 앱을 열었을 때 다른 사용자가 중단한 위치에서 계속 읽을 수 있도록 할 수 있습니다. iCloud를 사용하여 설정을 저장하는 경우, 사용자가 원하는 설정을 모든 장치에 적용해야 합니다. 예를 들어, 일부 설정은 집보다 회사에서 더 유용할 수 있습니다.
>




**Warn about the consequences of deleting a document.** When someone deletes a document in an iCloud-enabled app, the document is removed from iCloud and all other devices too. Show a warning and ask for confirmation before performing the deletion.
> 문서 삭제의 결과에 대해 경고합니다. iCloud 지원 앱에서 누군가가 문서를 삭제하면 해당 문서는 iCloud 및 다른 모든 장치에서도 제거됩니다. 삭제를 수행하기 전에 경고를 표시하고 확인을 요청합니다.
>




**Make conflict resolution prompt and easy.** To the extent possible, try to detect and resolve version conflicts automatically. If this can’t be done, display an unobtrusive notification that makes it easy to differentiate and choose between the conflicting versions. Conflict resolution should always occur as early as possible, so time isn’t wasted in the wrong version.
> 충돌을 신속하고 쉽게 해결하십시오. 가능한 한 버전 충돌을 자동으로 검색하고 해결하십시오. 이 작업을 수행할 수 없는 경우 쉽게 구분하고 충돌하는 버전을 선택할 수 있도록 눈에 띄지 않는 알림을 표시합니다. 충돌 해결은 항상 가능한 한 빨리 이루어져야 하므로 잘못된 버전에서 시간을 낭비하지 않습니다.
>




**Include iCloud content in search results.** People with iCloud accounts assume their content is universally available, and they expect search results to reflect this perspective.
> iCloud 컨텐츠를 검색 결과에 포함합니다. iCloud 계정을 가진 사람들은 자신의 컨텐츠가 보편적으로 사용 가능하다고 가정하며, 검색 결과가 이러한 관점을 반영할 것으로 기대합니다.
>



