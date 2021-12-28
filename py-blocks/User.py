import requests, random, webbrowser
from time import time
from typing import Union
import Utils

#Variables
RawCookie = None
UserID = None
Username = None
Robux = None
Thumbnail = None
isBuildersclub = None
isPremium = None
canChangeUsername = None
isAdmin = None
isEmailOnFile = None
isEmailVerified = None
isPhoneFeatureEnabled = None
isSuperSafePrivacyMode = None
IsAppChatSettingEnabled = None
IsGameChatSettingEnabled = None
IsContentRatingsSettingEnabled = None
IsParentalControlsTabEnabled = None
IsSetPasswordNotificationEnabled = None
ChangePasswordRequiresTwoStepVerification = None
ChangeEmailRequiresTwoStepVerification = None
UserEmail = None
UserEmailMasked = None
UserEmailVerified = None
CanHideInventory = None
CanTrade = None
MissingParentEmail = None
IsUpdateEmailSectionShown = None
IsUnder13UpdateEmailMessageSectionShown = None
IsUserConnectedToFacebook = None
IsTwoStepToggleEnabled = None
AgeBracket = None
UserAbove13 = None
ClientIpAddress = None
UserAge = None
IsBcRenewalMembership = None
IsAccountPinEnabled = None
IsAccountRestrictionsFeatureEnabled = None
IsAccountRestrictionsSettingEnabled = None
IsAccountSettingsSocialNetworksV2Enabled = None
InApp = None
HasFreeNameChange = None
IsAgeDownEnabled = None
ReceiveNewsletter = None

#Internal Commands
def SetCookie(Cookie: str, Details: bool = True) -> str:
    try:
        global RawCookie
        global CurrentCookie
        RawCookie = Cookie
        session = requests.session()
        CurrentCookie = {'.ROBLOSECURITY': Cookie}
        requests.utils.add_dict_to_cookiejar(session.cookies, CurrentCookie)
        Header = session.post('https://catalog.roblox.com/')
        session.headers['X-CSRF-TOKEN'] = Header.headers['X-CSRF-TOKEN']
        session.headers["Origin"] = "https://www.roblox.com"
        session.headers["Referer"] = "https://www.roblox.com/"
        CurrentCookie = session
        if(Utils.CheckCookie(CurrentCookie) == "Invalid"):
            return "Invalid Cookie"
        if(Details == True):
            GetDetails()
        else:
            GetDetails(False)
        return "Cookie Set"
    except:
        return "Error Setting Cookie"

def GetDetails(Details: bool = True) -> str:
    """
    Internal function to get the details of the current cookie, can be used if you have statements to determine if you want the details or not
    """
    global Gamesession
    global UserID
    global Username
    global Robux
    global Thumbnail
    global isBuildersclub
    global isPremium
    global canChangeUsername
    global isAdmin
    global isEmailOnFile
    global isEmailVerified
    global isPhoneFeatureEnabled
    global isSuperSafePrivacyMode
    global IsAppChatSettingEnabled
    global IsGameChatSettingEnabled
    global IsContentRatingsSettingEnabled
    global IsParentalControlsTabEnabled
    global IsSetPasswordNotificationEnabled
    global ChangePasswordRequiresTwoStepVerification
    global ChangeEmailRequiresTwoStepVerification
    global UserEmail
    global UserEmailMasked
    global UserEmailVerified
    global CanHideInventory
    global CanTrade
    global MissingParentEmail
    global IsUpdateEmailSectionShown
    global IsUnder13UpdateEmailMessageSectionShown
    global IsUserConnectedToFacebook
    global IsTwoStepToggleEnabled
    global AgeBracket
    global UserAbove13
    global ClientIpAddress #Shows the IP address roblox sees
    global UserAge
    global IsBcRenewalMembership
    global IsAccountPinEnabled
    global IsAccountRestrictionsFeatureEnabled
    global IsAccountRestrictionsSettingEnabled
    global IsAccountSettingsSocialNetworksV2Enabled
    global InApp
    global HasFreeNameChange
    global IsAgeDownEnabled
    global ReceiveNewsletter
    if(Details == True):
        try:
            SettingsContainer = CurrentCookie.get(Utils.SettingsURL)
            SettingsContainer = SettingsContainer.json()

            BasicContainer = CurrentCookie.get(Utils.MobileAPI + 'userinfo')
            BasicContainer = BasicContainer.json()

            UserID = BasicContainer['UserID']
            Username = BasicContainer['UserName']
            Robux = BasicContainer['RobuxBalance']
            Thumbnail = BasicContainer['ThumbnailUrl']
            isBuildersclub = BasicContainer['IsAnyBuildersClubMember']
            isPremium = BasicContainer['IsPremium']
            canChangeUsername = SettingsContainer['ChangeUsernameEnabled']
            isAdmin = SettingsContainer['IsAdmin']
            isEmailOnFile = SettingsContainer['IsEmailOnFile']
            isEmailVerified = SettingsContainer['IsEmailVerified']
            isPhoneFeatureEnabled = SettingsContainer['IsPhoneFeatureEnabled']
            isSuperSafePrivacyMode = SettingsContainer['UseSuperSafePrivacyMode']
            IsAppChatSettingEnabled = SettingsContainer['IsAppChatSettingEnabled']
            isGameChatSettingEnabled = SettingsContainer['IsGameChatSettingEnabled']
            isContentRatingsSettingEnabled = SettingsContainer['IsContentRatingsSettingEnabled']
            isParentalControlsTabEnabled = SettingsContainer['IsParentalControlsTabEnabled']
            isSetPasswordNotificationEnabled = SettingsContainer['IsSetPasswordNotificationEnabled']
            ChangePasswordRequiresTwoStepVerification = SettingsContainer['ChangePasswordRequiresTwoStepVerification']
            ChangeEmailRequiresTwoStepVerification = SettingsContainer['ChangeEmailRequiresTwoStepVerification']
            UserEmail = SettingsContainer['UserEmail']
            UserEmailMasked = SettingsContainer['UserEmailMasked']
            UserEmailVerified = SettingsContainer['UserEmailVerified']
            CanHideInventory = SettingsContainer['CanHideInventory']
            CanTrade = SettingsContainer['CanTrade']
            MissingParentEmail = SettingsContainer['MissingParentEmail']
            isUnder13UpdateEmailMessageSectionShown = SettingsContainer['IsUnder13UpdateEmailMessageSectionShown']
            isUserConnectedToFacebook = SettingsContainer['IsUserConnectedToFacebook']
            isUpdateEmailSectionShown = SettingsContainer['IsUpdateEmailSectionShown']
            isTwoStepToggleEnabled = SettingsContainer['IsTwoStepToggleEnabled']
            AgeBracket = SettingsContainer['AgeBracket']
            UserAbove13 = SettingsContainer['UserAbove13']
            ClientIpAddress = SettingsContainer['ClientIpAddress']
            UserAge = SettingsContainer['AccountAgeInDays']
            isBcRenewalMembership = SettingsContainer['IsBcRenewalMembership']
            isAccountPinEnabled = SettingsContainer['IsAccountPinEnabled']
            isAccountRestrictionsFeatureEnabled = SettingsContainer['IsAccountRestrictionsFeatureEnabled']
            isAccountRestrictionsSettingEnabled = SettingsContainer['IsAccountRestrictionsSettingEnabled']
            isAccountSettingsSocialNetworksV2Enabled = SettingsContainer['IsAccountSettingsSocialNetworksV2Enabled']
            InApp = SettingsContainer['InApp']
            HasFreeNameChange = SettingsContainer['HasFreeNameChange']
            isAgeDownEnabled = SettingsContainer['IsAgeDownEnabled']
            ReceiveNewsletter = SettingsContainer['ReceiveNewsletter']

            Gamesession = requests.session()
            Gamesession.cookies[".ROBLOSECURITY"] = RawCookie

            Gamesession = Gamesession.post(
            url = Utils.GameAuthUrl,
            headers = {
                "Referer": "https://www.roblox.com/",
                "X-CSRF-Token": Gamesession.post(
                    url = Utils.GameAuthUrl
                ).headers["X-CSRF-Token"],
            }
            ).headers["RBX-Authentication-Ticket"]

            return "Data Gathered"
        except Exception as e:
            return f"Error {e}"
    else:
        UserID = None
        Username = None
        Robux = None
        Thumbnail = None
        isBuildersclub = None
        isPremium = None
        canChangeUsername = None
        isAdmin = None
        isEmailOnFile = None
        isEmailVerified = None
        isPhoneFeatureEnabled = None
        isSuperSafePrivacyMode = None
        IsAppChatSettingEnabled = None
        IsGameChatSettingEnabled = None
        IsContentRatingsSettingEnabled = None
        IsParentalControlsTabEnabled = None
        IsSetPasswordNotificationEnabled = None
        ChangePasswordRequiresTwoStepVerification = None
        ChangeEmailRequiresTwoStepVerification = None
        UserEmail = None
        UserEmailMasked = None
        UserEmailVerified = None
        CanHideInventory = None
        CanTrade = None
        MissingParentEmail = None
        IsUpdateEmailSectionShown = None
        IsUnder13UpdateEmailMessageSectionShown = None
        IsUserConnectedToFacebook = None
        IsTwoStepToggleEnabled = None
        AgeBracket = None
        UserAbove13 = None
        ClientIpAddress #Shows the IP address roblox sees = None
        UserAge = None
        IsBcRenewalMembership = None
        IsAccountPinEnabled = None
        IsAccountRestrictionsFeatureEnabled = None
        IsAccountRestrictionsSettingEnabled = None
        IsAccountSettingsSocialNetworksV2Enabled = None
        InApp = None
        HasFreeNameChange = None
        IsAgeDownEnabled = None
        ReceiveNewsletter = None
        return "Data Not Wanted"

def isFollowing(targetUserID: int) -> Union[bool, str]:
    """
    Checks if the current account is following a user
    """
    try:
        response = CurrentCookie.get(f"{Utils.APIURL}user/following-exists?UserID={str(targetUserID)}&followerUserID={UserID}", data={'targetUserID': targetUserID})
        return response.json()['isFollowing']
    except Exception as e:
        return e

def FollowUser(targetUserID: int) -> Union[bool, str]:
    """
    Follows a user
    """
    try:
        response = CurrentCookie.post(f"{Utils.FriendsAPI}{str(targetUserID)}/follow", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return e

def UnfollowUser(targetUserID: int) -> Union[dict, str]:
    """
    unfollows a user
    """
    try:
        response = CurrentCookie.post(f"{Utils.FriendsAPI}{str(targetUserID)}/unfollow", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def BlockUser(targetUserID: int) -> Union[bool, str]:
    """
    Blocks a user
    """
    try:
        response = CurrentCookie.post(f"{Utils.APIURL}userblock/block?userId={str(targetUserID)}", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def GetBlockedUsers() -> Union[tuple, dict]:
    """
    Returns users which are blocked
    [UserID],[UserName]
    """
    try:
        response = CurrentCookie.get(f"{Utils.SettingsURL}")
        Data = response.json()['BlockedUsersModel']['BlockedUsers']
        BlockedIDs = []
        BlockedNames = []

        for User in Data:
            BlockedIDs.append(User['uid'])
            BlockedNames.append(User['Name'])
        return BlockedIDs, BlockedNames
    except:
        return response.json()

def UnblockUser(targetUserID: int) -> Union[bool, dict]:
    """
    unblocks a user
    """
    try:
        #response = CurrentCookie.post(f"{Utils.APIURL}userblock/unblock?userId={str(targetUserID)}", data={'targetUserID': targetUserID})
        response = CurrentCookie.post(f"https://accountsettings.roblox.com/v1/users/{targetUserID}/unblock", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def SendMessage(targetUserID: int, Subject: str, Body: str) -> Union[str, dict]:
    """
    Sends the given message to the given user
    """
    response = None
    try:
        response = CurrentCookie.post(Utils.PrivateMessageAPIV1 + 'messages/send/', data={
                            'userId': UserID,
                            'subject': Subject,
                            'body': Body,
                            'recipientid': targetUserID,
                            })
        return response.json()['message']
    except Exception as e:
        return response.json()

def JoinGame(PlaceId: int) -> None:
    """
    Joins the given game
    """
    BrowserID = random.randint(10000000000, 99999999999)
    webbrowser.open(f"roblox-player:1+launchmode:play+gameinfo:{Gamesession}+launchtime:{int(time()*1000)}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{BrowserID}%26placeId%3D{PlaceId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{BrowserID}+robloxLocale:en_us+gameLocale:en_us")

# External

def GetID(Username: str) -> Union[int, str]:
    """
    Returns the ID of a user based on the username
    """
    response = requests.get(
        Utils.APIURL + f'users/get-by-username?username={Username}')
    try:
        return response.json()['Id']
    except:
        return response.json()['errorMessage']

def GetUserName(UserID: int) -> str:
    """
    Returns the username of a user based on the ID
    """
    response = requests.get(Utils.UserAPI + f"{str(UserID)}")
    try:
        return response.json()['Username']
    except:
        return "Unable to convert ID"

def UsernameHistory(UserID: int) -> Union[list, str]:
    """
    Returns an array of previous usernames as user has had
    """
    Cursor = ""
    Done = False
    PastNames = []
    while(Done == False):
        response = requests.get(Utils.UserAPIV1 + f"{UserID}/username-history?limit=100&sortOrder=Asc&cursor={Cursor}")
        Names = response.json()['data']
        if((response.json()['nextPageCursor'] == "null") or response.json()['nextPageCursor'] == None):
            Done = True
        else:
            Done = False
            Cursor = response.json()['nextPageCursor']
        for Name in Names:
            PastNames.append(Name['name'])
        if(response.json()['nextPageCursor'] == 'None'):
            Done = True
    return PastNames

def IsOnline(UserID: int) -> Union[bool, str]:
    """
    Returns whether a user is online
    """
    response = requests.get(Utils.UserAPI + str(UserID) +"/onlinestatus")
    try:
        return response.json()['IsOnline']
    except:
        return 'User not found'

def Isbanned(UserID: int) -> Union[bool, str]:
    """
    Returns if a user account is currently banned
    """
    response = requests.get(Utils.UserAPIV1 + str(UserID))
    try:
        return response.json()['isBanned']
    except:
        return 'User not found'

def GetDescription(UserID: int) -> str:
    """
    Returns the description of a given user
    """
    response = requests.get(Utils.UserAPIV1 + str(UserID))
    try:
        return response.json()['description']
    except:
        return 'User not found'

def GetAge(UserID: int) -> str:
    """
    Returns the user's age in days
    """
    response = requests.get(Utils.UserAPIV1 + str(UserID))
    try:
        CreationDate = response.json()['created']
        CreationDate = CreationDate.split('T')
        CreationDate = CreationDate[0].split('-')
        CreationDate = datetime.date(int(CreationDate[0]), int(CreationDate[1]), int(CreationDate[2]))
        Days = ((datetime.date.today()) - (CreationDate))
        Days = str(Days).split(' ')
        return Days[0]
    except:
        return (Utils.UserAPIV1 + str(UserID))

def CreationDate(UserID: int, Style: int = 0) -> str:
    """
    Returns the date a user was created
    StandardFormat: dd/mm/yyyy
    Americans: mm/dd/yyyy
    If you wish you to use the American format set the 'Style' Vairable to 1
    """
    response = requests.get(Utils.UserAPIV1 + str(UserID))
    try:
        CreationDate = response.json()['created']
        CreationDate = CreationDate.split('T')
        CreationDate = CreationDate[0].split('-')
        if(Style == 0):
            return (str(CreationDate[2]) + '/' + str(CreationDate[1]) + '/' + str(CreationDate[0])) #DD/MM/YYYY -- The Correct Format
        else:
            return (str(CreationDate[1]) + '/' + str(CreationDate[2]) + '/' + str(CreationDate[0])) #MM/DD/YYYY -- Those Colonists Format
    except:
        return response.json()['errors'][0]['message']

def GetRAP(UserID: int) -> int:
    """
    Returns the total offical roblox RAP value for a user
    Please be aware this function can take some time to run depending on internet speed and how many limiteds a user owns
    """
    ErroredRAP = 0
    TotalValue = 0
    Cursor = ""
    Done = False
    while(Done == False):
        try:
            response = requests.get(Utils.Inventory1URL + f"/{UserID}/assets/collectibles?sortOrder=Asc&limit=100&cursor={Cursor}")
            Items = response.json()
            if((response.json()['nextPageCursor'] == "null") or response.json()['nextPageCursor'] == None):
                Done = True
            else:
                Done = False
                Cursor = response.json()['nextPageCursor']
            for Item in Items["data"]:
                try:
                    RAP = int((Item['recentAveragePrice']))
                    TotalValue = TotalValue + RAP
                except:
                    TotalValue = TotalValue
            if(response.json()['nextPageCursor'] == 'None'):
                Done = True
            
        except Exception as ex:
            Done = True
    return(TotalValue)

def GetLimiteds(UserID: int) -> tuple:
    """
    Returns the total list of a users limiteds
    Please be aware this function can take some time to run depending on internet speed and how many limiteds a user owns
    """
    Limiteds = []
    IDs = []
    Cursor = ""
    Done = False
    while(Done == False):
        try:
            response = requests.get(Utils.Inventory1URL + f"/{UserID}/assets/collectibles?sortOrder=Asc&limit=100&cursor={Cursor}")
            Items = response.json()
            if((response.json()['nextPageCursor'] == "null") or response.json()['nextPageCursor'] == None):
                Done = True
            else:
                Done = False
                Cursor = response.json()['nextPageCursor']
            for Item in Items["data"]:
                try:
                    Limited = Item['name']
                    ID = Item['assetId']
                    Limiteds.append(Limited)
                    IDs.append(ID)
                except:
                    Limiteds = Limiteds
                    IDs = IDs
            if(response.json()['nextPageCursor'] == 'None'):
                Done = True
            
        except Exception as ex:
            Done = True
    return(Limiteds,IDs)

def GetBust(UserID: int, Width: int = 420, Height: int = 420) -> str:
    """
    Returns the link to a bust image of a user
    Width and Height can be customised
    """
    response = requests.get(f"https://www.roblox.com/bust-thumbnail/image?userId={UserID}&width={Width}&height={Height}&format=png")
    return response.url

def GetHeadshot(UserID: int, Width: int = 420, Height: int = 420) -> str:
    """
    Returns the link to a headshot image of a user
    Width and Height can be customised
    """
    response = requests.get(f"https://www.roblox.com/headshot-thumbnail/image?userId={UserID}&width={Width}&height={Height}&format=png")
    return response.url

def GetStatus(UserID: int) -> str:
    """
    Returns the current status of a user
    """
    response = requests.get(Utils.UserAPIV1 + f"{str(UserID)}/status")
    return response.json()['status']

def DoesNameExist(Username: str) -> Union[bool, dict]:
    """
    Returns wether or not the given username is taken
    """
    response = requests.get(Utils.APIURL + 'users/get-by-username?username=' + str(Username))
    try:
        if('errorMessage' in response.text):
            return False
        else:
            if(response.json()['Username'].lower() == Username.lower()):
                return True
            elif (response.json()['Username'].lower() != Username.lower()):
                return False
    except:
        return response.json()
