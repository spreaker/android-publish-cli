# Android publish tool

A simple but effective command line tool to programmatically release updated APK for existing Android apps


## Installation
To install, simply use `pip` or `easy_install`:

```
$ pip install --upgrade android-publish-cli
```

or

```
$ easy_install --upgrade android-publish-cli
```


## Python Version
Python 2.6 or 2.7 is required. Python 3.x is not yet supported.


## Prerequisites

This tools works only with Google Service Accounts, not generic OAuth clients. A Service Account is an Oauth2 account specifically created for server-to-server communication. You create an account once, store the credentials on your servers, and use those credentials to authenticate api requests.

Follow [this guide](https://developers.google.com/android-publisher/getting_started) to create a new service account in your Google Play Developer console. At the end of the process you will get an email address and a .p12 private key. Safely store this informations and you are ready to go!

## Usage

```
positional arguments:
  apk                   The APK filepath

other arguments:
  --email/-e EMAIL      The service account email
  --key/-k KEY          The key filepath
  --package/-p PACKAGE  The package name. Example: com.android.sample
  --track/-t TRACK      The track. Could be 'alpha', beta', 'production' or 'rollout' (optional, default: production)
  --changes/-c CHANGES  Recent changes (optional)
```

## Example

```
$ android-publish
  --email "your.service.account.email@developer.gserviceaccount.com" \
  --key "/path/to/your/service/account/key/file.p12" \
  --package "com.yourcompany.yourapp" \
    --track "production" \
    --changes "Updated the app for Android 5.0" \
    "/path/to/your/apk/file.apk"
```


