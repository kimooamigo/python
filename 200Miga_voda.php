<?php

$number = readline("Enter Your Number > ");
sleep(2);
echo "\n";
$pwd = readline("Enter Your Password > ");

$session = curl_init();

function generationLink($stringLingth)
{
    $latters = "abcdefghijklmnopqrstuvwxyz";
    return substr(str_shuffle($latters), 0, $stringLingth);
}

$urlLoginPage = "https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce=" . generationLink(10) . "&kc_locale=en";

curl_setopt($session, CURLOPT_URL, $urlLoginPage);
curl_setopt($session, CURLOPT_RETURNTRANSFER, true);

$responsePageLogin = curl_exec($session);

$soup = new DOMDocument();

@$soup->loadHTML(mb_convert_encoding($responsePageLogin, 'HTML-ENTITIES', 'UTF-8'));

$form = $soup->getElementsByTagName('form')->item(0);
$getUrlAction = $form->getAttribute('action');

$headerRequest = [
    'Accept' => 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding' => 'gzip, deflate, br',
    'Accept-Language' => 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
    'Connection' => 'keep-alive',
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Host' => 'web.vodafone.com.eg',
    'Origin' => 'https://web.vodafone.com.eg',
    'Referer' => $urlLoginPage,
    'User-Agent' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
];

$formData = [
    'username' => $number,
    'password' => $pwd
];

curl_setopt($session, CURLOPT_POST, true);
curl_setopt($session, CURLOPT_POSTFIELDS, $formData);
curl_setopt($session, CURLOPT_HTTPHEADER, $headerRequest);

$sendUserData = curl_exec($session);
$checkRegistry = curl_getinfo($session, CURLINFO_EFFECTIVE_URL);
$_checkRegistry = strpos($checkRegistry, 'KClogin');

if ($_checkRegistry != -1) {
    $code = $checkRegistry;
    $_code = substr($code, strpos($code, 'code=') + 5);
    $headerAccessToken = [
        'Accept' => '*/*',
        'Accept-Encoding' => 'gzip, deflate, br',
        'Accept-Language' => 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
        'Connection' => 'keep-alive',
        'Content-type' => 'application/x-www-form-urlencoded',
        'Host' => 'web.vodafone.com.eg',
        'Origin' => 'https://web.vodafone.com.eg',
        'Referer' => 'https://web.vodafone.com.eg/ar/KClogin',
        'User-Agent' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    ];
    $formDataAccessToken = [
        'code' => $_code,
        'grant_type' => 'authorization_code',
        'client_id' => 'website',
        'redirect_uri' => 'https://web.vodafone.com.eg/ar/KClogin'
        ]
        curl_setopt($session, CURLOPT_POST, true);
        curl_setopt($session, CURLOPT_POSTFIELDS, $formDataAccessToken);
        curl_setopt($session, CURLOPT_HTTPHEADER, $headerAccessToken);
        $sendDataAccessToken = curl_exec($session);
        
$jwt = json_decode($sendDataAccessToken, true)['access_token'];
$url = "https://mobile.vodafone.com.eg:443/mobile-app/promo/unifiedRedeemPromo";
$headers = [
    "Authorization" => "Bearer " . $jwt,
    "operatingSystem" => "V11.0.8.0.PCOMIXM",
    "platform" => "Android",
    "deviceType" => "ginkgo",
    "buildNumber" => "414",
    "Content-Type" => "application/json; charset=UTF-8",
    "Connection" => "close",
    "Accept-Encoding" => "gzip, deflate",
    "User-Agent" => "okhttp/3.12.1"
];
$json = [
    "channelId" => 3,
    "contextualOperationId" => 0,
    "contextualPromoId" => 0,
    "operationId" => 0,
    "param1" => "Vodafone",
    "promoId" => 3336,
    "triggerId" => 332,
    "triggerType" => "6",
    "wlistId" => 3256
];

curl_setopt($session, CURLOPT_POST, true);
curl_setopt($session, CURLOPT_POSTFIELDS, $json);
curl_setopt($session, CURLOPT_HTTPHEADER, $headers);
$response = curl_exec($session);
$g = json_decode($response, true)['giftQuota'];

if ($g == "200") {
    echo "Done Login ";
    sleep(2);
    echo "DONE ADD 200MG";
} else {
    echo "Done Login ";
    sleep(2);
    echo "Try Later";
}
?>