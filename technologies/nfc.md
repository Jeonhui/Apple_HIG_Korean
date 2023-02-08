# **[technologies] nfc**

# Near-field communication (NFC) enables devices within a few centimeters of each other to exchange information wirelessly.
> 근거리 무선 통신(NFC)은 서로 몇 센티미터 이내의 장치들이 무선으로 정보를 교환할 수 있게 한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-nfc-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-nfc-intro_2x.png)

iOS apps running on supported devices can use NFC scanning to read data from electronic tags attached to real-world objects. For example, a user can scan a toy to connect it with a video game, a shopper can scan an in-store sign to access coupons, or a retail employee can scan products to track inventory.
> 지원되는 장치에서 실행되는 iOS 앱은 NFC 스캐닝을 사용하여 실제 객체에 부착된 전자 태그에서 데이터를 읽을 수 있습니다. 예를 들어, 사용자는 장난감을 스캔하여 비디오 게임과 연결할 수 있고, 쇼핑객은 매장 내 표지판을 스캔하여 쿠폰에 액세스할 수 있으며, 소매점 직원은 제품을 스캔하여 재고를 추적할 수 있습니다.
>




# **In-app tag reading**

An app can enable single- or multiple-object scanning when the app is active, and display a scanning sheet whenever the user is expected to scan something.
> 앱은 앱이 활성화되어 있을 때 단일 또는 다중 개체 검색을 활성화할 수 있으며, 사용자가 무언가를 검색할 것으로 예상될 때마다 검색 시트를 표시할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/nfc/images/nfc-ready-to-scan_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/nfc/images/nfc-ready-to-scan_2x.png)

**Don't encourage people to make contact with physical objects.** To scan a tag, an iOS device must simply be within close proximity of the tag. It doesn't need to actually touch the tag. Use terms like *scan* and *hold near* instead of *tap* and *touch* when asking people to scan objects.
> 태그를 스캔하려면 iOS 장치가 태그에서 가까운 곳에 있어야 합니다. 실제로 태그를 터치할 필요가 없습니다. 사람들에게 물체를 스캔하도록 요청할 때 탭 앤 터치 대신 스캔 및 근처에 대기와 같은 용어를 사용합니다.
>




**Use approachable terminology.** Near-field communication may be unfamiliar to some people. To make it approachable, avoid referring to technical, developer-oriented terms like *NFC*, *Core NFC*, *Near-field communication*, and *tag*. Instead, use friendly, conversational terms that most people will understand.
> 접근 가능한 용어를 사용하십시오. 근거리 무선 통신은 일부 사람들에게 생소할 수 있습니다. 접근 가능하게 하려면 근거리 무선 통신, 코어 근거리 무선 통신, 근거리 무선 통신 및 태그와 같은 기술적, 개발자 지향적 용어를 언급하지 않는다. 대신, 대부분의 사람들이 이해할 수 있는 친근하고 대화가 가능한 용어를 사용하세요.
>




| Use | Don't use |
| --- | --- |
| Scan the [object name]. | Scan the NFC tag. |
| Hold your iPhone near the [object name] to learn more about it. | To use NFC scanning, tap your phone to the [object]. |

**Provide succinct instructional text for the scanning sheet.** Provide a complete sentence, in sentence case, with ending punctuation. Identify the object to scan, and revise the text appropriately for subsequent scans. Keep the text short to avoid truncation.
> 스캔 시트에 대한 간결한 지침 텍스트를 제공하십시오. 문장의 경우 끝에 구두점이 있는 완전한 문장을 제공하십시오. 검색할 개체를 식별하고 이후 검색에 적합하게 텍스트를 수정합니다. 잘라내기를 방지하려면 텍스트를 짧게 유지하십시오.
>




| First scan | Subsequent scans |
| --- | --- |
| Hold your iPhone near the [object name] to learn more about it. | Now hold your iPhone near another [object name]. |

# **Background tag reading**

Background tag reading lets people scan tags quickly any time, without needing to first open your app and initiate scanning. On devices that support background tag reading, the system automatically looks for nearby compatible tags whenever the screen is illuminated. After detecting and matching a tag with an app, the system shows a notification that the user can tap to send the tag data to the app for processing. Note that background reading is disabled when an NFC scanning sheet is visible, Wallet or Apple Pay are in use, cameras are in use, the device is in airplane mode, and the device is locked after a restart.
> 백그라운드 태그 읽기를 사용하면 먼저 앱을 열고 검색을 시작할 필요 없이 언제든지 빠르게 태그를 검색할 수 있습니다. 백그라운드 태그 읽기를 지원하는 장치에서는 화면이 켜질 때마다 시스템이 자동으로 근처의 호환 가능한 태그를 찾습니다. 태그를 감지하여 앱과 매칭한 후, 시스템은 사용자가 탭하여 태그 데이터를 앱으로 전송하여 처리할 수 있다는 알림을 보여준다. 근거리 무선 통신 스캔 시트가 보이고, 지갑 또는 애플 페이가 사용 중이며, 카메라가 사용 중이며, 장치가 비행기 모드에 있으며, 다시 시작한 후 장치가 잠겨 있으면 백그라운드 판독이 비활성화됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/nfc/images/nfc-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/nfc/images/nfc-background_2x.png)

**Support both background and in-app tag reading.** Your app must still provide an in-app way to scan tags, for people with devices that don't support background tag reading.
> 백그라운드 태그 읽기와 앱 내 태그 읽기를 모두 지원합니다. 백그라운드 태그 읽기를 지원하지 않는 장치를 사용하는 사람들을 위해 앱 내에서 태그를 검색할 수 있는 방법을 제공해야 합니다.
>



