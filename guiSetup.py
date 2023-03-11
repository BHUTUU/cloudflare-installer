#Documentation section------->>>
'''
Package: Cloudflare Gui
Objective: To setup cloudflare in windows and linux with graphical User Interface.
Author: Suman Kumar ~BHUTUU
Github: https://github.com/BHUTUU/cloudflare-installer
Date: Bahut time lag gya hai bro ab date yaaad nhi hai. Aaj dhyan aaya hai ki documentation v likhna hota hai XD
'''
import os, requests, webbrowser, platform
from time import sleep as sleep
from tkinter import *
from PIL import Image, ImageTk
#<<<------Internal Variables----->>>
OS = str(os.name)
if OS.upper() == 'NT':
    architecture = platform.machine()
    realName = "windows"
    downloadFolder = os.path.expanduser('~')+"/Downloads"
    programDir = 'C:/Program Files'
    gitDir = 'C:/Program Files/Git/usr/bin'
elif OS.upper() == 'POSIX' or OS.upper() == 'GNU/LINUX' or OS.upper() == 'LINUX':
    realName = "GNU/Linux"
    architecture = platform.machine()
    homeDir = os.path.expanduser('~')
    rootDir = '/usr'
    pathDir = '/usr/bin'
#<<<-----Functions----->>>
def internetCheck():
    try:
        requests.get("https://google.com/")
        return True
    except:
        return False

def internetCheckDialogBox():
    val = None
    internetBox = Tk()
    #<<<---Bix dimentioning----->>>
    internetBox.geometry("500x400")
    internetBox.minsize(500, 400)
    # internetBox.maxsize(400, 400)
    #<<<-----Title bar -- icon and title name---->>>
    iconPhoto = PhotoImage(file='cloudIcon.png')
    internetBox.iconphoto(False, iconPhoto)
    internetBox.title("Cloudflared-Installer")
    def onCloseTrue():
        val = True
        internetBox.destroy()
        return True
    def onCloseFalse():
        internetBox.destroy()
        return False
    if internetCheck():
        message = 'Internet connection status:'
        message1 = 'Connected'
        messageLabel = Label(internetBox, text=message, highlightcolor="pink", highlightthickness=3).pack(pady=[80,0])
        message1Label = Label(internetBox, text=message1, highlightcolor="pink", highlightthickness=3).pack(pady=[20,0])
        setupStartButton = Button(internetBox, text="Continue", highlightthickness=5, highlightcolor="grey", command=onCloseTrue).pack(pady=[10,0])
        val = True
    else:
        message = "check your internet connection!"
        message1 = "Try again with good internet connection!!"
        messageLabel = Label(internetBox, text=message, highlightcolor="pink", highlightthickness=3).pack(pady=[80,0])
        closeButton = Button(internetBox, text="Close", highlightcolor="grey", highlightthickness=5, command=onCloseFalse).pack(pady=[10,0])
        val = False
    internetBox.mainloop()
    return val

def mainDialogBox():
    def onCloseALL():
        winRoot.destroy()
    winRoot = Tk()
    #<<<---Box dimentioning----->>>
    winRoot.geometry("700x500")
    winRoot.minsize(700,500)
    winRoot.maxsize(800,600)
    #<<<---Title bar -- icon and title name---->>>
    iconPhoto = PhotoImage(file='cloudIcon.png')
    winRoot.iconphoto(False, iconPhoto)
    winRoot.title("Cloudflared-Installer")
    #<<---Frames--->>
    #introFrame
    introFrame = Frame(winRoot,bg="white", height=200, highlightbackground="pink", highlightthickness=5)
    introFrame.pack(side=TOP, fill=X, padx=20, pady=[20,0])
    #Introduction text
    introText = '''Welcome to cloudflare GUI
    Author: Suman Kumar ~BHUTUU'''
    introLabel = Label(introFrame, text=introText, bg="white")
    introLabel.pack()
    #Cloudflare Image
    cloudImage = Image.open("cloudIcon.png")
    resizedCloudImage= cloudImage.resize((100,100), Image.LANCZOS)
    plugCloudImage = ImageTk.PhotoImage(resizedCloudImage)
    cloudImageLable = Label(introFrame, image=plugCloudImage, bg="white")
    cloudImageLable.pack(side=LEFT, padx=[50,0])
    #Bhutuu Image
    bhutuuImage = Image.open("bhutuu.png")
    resizedBhutuuImage = bhutuuImage.resize((100,100), Image.LANCZOS)
    plugBhutuuImage = ImageTk.PhotoImage(resizedBhutuuImage)
    bhutuuImageLable = Label(introFrame, image=plugBhutuuImage, bg="white")
    bhutuuImageLable.pack(side=RIGHT, padx=[0,50])
    #Terms and conditions frame
    termsAndConditionFrame = Frame(winRoot, bg="white", highlightbackground="pink", highlightthickness=3)
    termsAndConditionFrame.pack(fill="x", padx=10, pady=10)
    scrollView = Scrollbar(termsAndConditionFrame)
    scrollView.pack(fill="y", side=RIGHT) 
    myList = Listbox(termsAndConditionFrame, yscrollcommand=scrollView.set)
    termsAndConditions = [
        "Cloudflare Website and Online Services Terms of Use".upper(), "", "",
        "Effective June 27, 2022", "",
        'Welcome to Cloudflare! As used in these Terms of Use, "Cloudflare", "us" or "we"',
        'refers to Cloudflare, Inc. and its affiliates.',
        '___________________________________________________________________________________________________________','',
        'PLEASE READ THE FOLLOWING CAREFULLY AS IT AFFECTS YOUR LEGAL RIGHTS. These terms of use',
        '(“Terms”),along with Cloudflare’s Privacy Policy, govern your use of Cloudflare’s Websites and Online',
        ' Services. For the purposes of these Terms, (i) “Websites” refers to www.cloudflare.com, as well as the',
        'other websites that Cloudflare operates and that link to these Terms, and (ii) “Online Services” means',
        'Cloudflare’s products and services that are publicly available without a subscription or a Cloudflare',
        'account, including, but not limited to, the 1.1.1.1 Public DNS Resolver service, including 1.1.1.1 for',
        'Families, Cloudflare Time Services, RPKI Portal, and Distributed Web Gateway and Resolver.',
        'If you do not agree to these Terms, you must not access or use our Websites or Online Services.','',
        'THESE TERMS DO NOT APPLY TO YOUR ACCESS AND USE OF THE CLOUDFLARE PRODUCTS'.upper(),
        'AND SERVICES THAT ARE PROVIDED UNDER THE SELF-SERVE SUBSCRIPTION AGREEMENT,'.upper(),
        'THE ENTERPRISE ,SUBSCRIPTION AGREEMENT OR OTHER WRITTEN AGREEMENT SIGNED'.upper(),
        'BETWEEN YOU AND CLOUDFLARE (IF APPLICABLE).'.upper(),'','',
        'If there is a conflict between these Terms and additional terms applicable to a',
        'given Website or Online Service, the additional terms will control for that conflict.','','',
        '1. ELIGIBILITY','','',
        'By agreeing to these Terms, you represent and warrant to us:',
        '   (i) that you are at least eighteen (18) years of age;',
        '   (ii) that you have not previously been suspended or',
        '        removed from the Websites and Online Services and',
        '   (iii) that your use of the Websites and Online Services is',
        '         in compliance with any and all applicable laws and regulations.','','',
        '2. LICENSE GRANT TO CLOUDFLARE','','',
        'By submitting, posting, or publishing your content, suggestions, enhancement requests,',
        'recommendations, feedback, information, data, or comments (“Content”) to any Website or',
        'Online Service, you are granting Cloudflare a perpetual, irrevocable, worldwide,',
        'non-exclusive, royalty-free right and license (with the right to sublicense) to use,',
        'incorporate, exploit, display, perform, reproduce, distribute, and prepare derivative',
        'works of your Content. You will retain ownership of your Content, however, any use of',
        'your Content by Cloudflare may be without any compensation paid to you. By submitting,',
        'posting, and publishing your Content, you represent and warrant that your Content, does not:',
        '   (i) infringe, violate, or misappropriate any third-party right, including any copyright,',
        '       trademark, patent, trade secret, moral right, privacy right, right of publicity, or any',
        '       other intellectual property or proprietary right; or (ii) slander, defame, or libel any third-party.','','',
        '3. INFRINGEMENT AND ABUSE','','',
        'With respect to the Online Services, Cloudflare operates pass-through network services used to improve',
        'network performance, not hosting provider services and as such, we have no way of removing improper or',
        'infringing material from our users’ websites, third party sites or their hosting services. Cloudflare has',
        'no control over any decentralized name registries, and cannot remove material that is accessible through',
        'the Distributed Web Gateway. Copyright holders or their agents concerned with material served through',
        'Cloudflare’s network should submit a notification of claimed copyright infringement or other abuse through',
        'our automated form located at https://www.cloudflare.com/abuse/.If you would prefer not to use our complaint',
        'submission form, you may mail your complaint to','','',
        'Cloudflare, Inc.',
        'Attn: Legal Department',
        '101 Townsend St,',
        'San Francisco, CA 94107','','',
        'When submitting abuse reports, please provide detailed information supporting your complaint as',
        'well as an affidavit attesting to its validity. Please bear in mind that unless you have',
        'requested us not to share your information through the opt-out procedure described on our',
        'abuse page, Cloudflare may provide copies of, or information from your notification or',
        'complaint to anyone it considers appropriate, including but not limited to the Cloudflare user whom the',
        'notification or complaint relates to, the Cloudflare user’s hosting provider, website operator and',
        'visitors of Cloudflare’s own website. For more information about how Cloudflare handles complaints',
        'please visit https://www.cloudflare.com/abuse/ .','','',
        'If you intend to automate the process by which you submit abuse reports , you will need to request',
        'access to an abuse API token. If you are granted an abuse API token, you agree not to disclose or',
        'provide the abuse API token to any person or entity other than to yourself or your organization’s',
        'employees, or use the API or API token in any manner prohibited under Section 7 below. You understand',
        'that Cloudflare may suspend or revoke an abuse API token at any time in Cloudflare’s reasonable discretion.','',''
        '4. TERMINATION OF USE; DISCONTINUATION AND MODIFICATION OF THE WEBSITES AND ONLINE SERVICES','','',
        'We may at our sole discretion suspend or terminate your access to the Websites and/or Online Services',
        'at any time, with or without notice for any reason or no reason at all. We also reserve the right to',
        'modify or discontinue the Websites and/or Online Services at any time (including, without limitation,',
        'by limiting or discontinuing certain features of the Websites and/or Online Services) without',
        'notice to you. We will have no liability whatsoever on account of any change to the Websites and/or',
        'Online Services or any suspension or termination of your access to or use of the Websites',
        'and/or Online Services.','','',
        '5. THIRD-PARTY WEBSITES','','',
        'The Websites and Online Services may contain links to third-party websites. Such linked websites',
        'are not under our control, and we are not responsible for their content','','',
        '6. OWNERSHIP; PROPRIETARY RIGHTS','','',
        'The visual interfaces, graphics, design, compilation, information, data,',
        'computer code (including source code or object code), products, software, services,',
        'and all other elements of the Websites and Online Services (the “Materials”) provided by',
        'Cloudflare are protected by all relevant intellectual property and proprietary rights and',
        'applicable laws. All Materials contained in the Websites and Online Services are the property',
        'of Cloudflare or our third-party licensors. Except as expressly authorized by Cloudflare you may',
        'not make use of the Materials. Cloudflare reserves all rights to the Materials',
        'not granted expressly in these Terms.','','',
        '7. PROHIBITED USES','','',
        'As a condition of your use of the Websites and Online Services, you will not use the Websites',
        'or Online Services for any purpose that is unlawful or prohibited by these Terms. You may not use',
        'the Websites or Online Services in any manner that could damage, disable, overburden, disrupt or',
        'impair any Cloudflare servers or APIs, or any networks connected to any Cloudflare server or APIs,',
        "or that could interfere with any other party's use and enjoyment of any Websites or Online Services.",
        'You may not transmit any viruses, worms, defects, Trojan horses, or any items of a destructive nature',
        'through your use of Websites or Online Services. You may not exceed or circumvent, or try to exceed or',
        'circumvent, limitations on the Websites or Online Services, including on any API calls, or otherwise',
        'use the Websites or Online Services in a manner that violates any Cloudflare documentation or user manuals.',
        'You may not attempt to gain unauthorized access to any Websites or Online Services, other accounts, computer',
        'systems, or networks connected to any Cloudflare server or to any of the Websites or Online Services through',
        'hacking, password mining, or any other means. You may not obtain or attempt to obtain any materials or',
        'information through any means not intentionally made available through the Websites or Online Services.',
        'You may not to use the Websites or Online Services in any way that violates any applicable federal, state,',
        'local, or international law or regulation (including, without limitation, any laws regarding the export of data',
        'or software to and from the US or other countries).','','',
        'Cloudflare retains the right (but not the obligation) to block content from its Distributed Web Gateway that',
        'Cloudflare determines (in its sole discretion) to be illegal, harmful, or in violation of these Terms. For these',
        'purposes, illegal or harmful content includes but is not limited to: (a) content containing, promoting, or',
        'facilitating child sexual abuse material or human trafficking; (b) content that infringes on another person’s',
        'intellectual property rights or is otherwise unlawful; (c) content that discloses sensitive personal information,',
        'incites or exploits violence, or is intended to defraud the public; and (d) content that seeks to distribute',
        'malware, facilitate phishing, or otherwise constitutes technical abuse','','',
        '8. INDEMNITY','','',
        'You agree that you will be responsible for your use of the Websites and Online Services, and you agree to',
        'defend, indemnify, and hold harmless Cloudflare and its officers, directors, employees, consultants, affiliates,',
        'subsidiaries and agents (collectively, the "Cloudflare Entities") from and against any and all claims, liabilities,',
        "damages, losses, and expenses, including reasonable attorneys' fees and costs, arising out of or in any way",
        'connected with',
        '   (i) your access to, use of, or alleged use of the Websites and Online Services;',
        '   (ii) your violation of these Terms or any representation, warranty, or agreements',
        '        referenced herein, or any applicable law or regulation;',
        '   (iii) your violation of any third-party right, including without limitation any intellectual property right,',
        '         publicity, confidentiality, property or privacy right; or (iv) any disputes or issues between you and any',
        '         third party. We reserve the right, at our own expense, to assume the exclusive defense and control of any',
        '         matter otherwise subject to indemnification by you (and without limiting your indemnification obligations with',
        '         respect to such matter), and in such case, you agree to cooperate with our defense of such claim.','','',
        '9 DISCLAIMERS; NO WARRANTIES','','',
        'THE WEBSITES AND ONLINE SERVICES ARE MADE AVAILABLE TO YOU ON AN "AS IS" AND "AS AVAILABLE" BASIS,',
        'WITH THE EXPRESS UNDERSTANDING THAT THE CLOUDFLARE ENTITIES HAVE NO OBLIGATION TO MONITOR, CONTROL, OR',
        'VET THE CONTENT OR DATA APPEARING ON THE WEBSITES AND ONLINE SERVICES. AS SUCH, YOUR USE OF THE WEBSITES',
        'AND ONLINE SERVICES IS AT YOUR OWN DISCRETION AND RISK. THE CLOUDFLARE ENTITIES MAKE NO CLAIMS OR PROMISES',
        'ABOUT THE QUALITY, ACCURACY, OR RELIABILITY OF THE WEBSITES AND ONLINE SERVICES AND EXPRESSLY DISCLAIM ALL',
        'WARRANTIES, WHETHER EXPRESS OR IMPLIED, INCLUDING IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR',
        'A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.','','',
        '10. LIMITATION OF LIABILITY','','',
        'IN NO EVENT WILL THE CLOUDFLARE ENTITIES BE LIABLE TO YOU OR ANY THIRD PARTY FOR ANY DIRECT, INDIRECT,',
        'INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES ARISING OUT OF OR RELATING TO YOUR ACCESS TO OR',
        'USE OF, OR YOUR INABILITY TO ACCESS OR USE, THE WEBSITES AND ONLINE SERVICES OR ANY MATERIALS OR CONTENT',
        'ON THE WEBSITES AND ONLINE SERVICES, WHETHER BASED ON WARRANTY, CONTRACT, TORT (INCLUDING NEGLIGENCE),',
        'STATUTE, OR ANY OTHER LEGAL THEORY, WHETHER OR NOT THE CLOUDFLARE ENTITIES HAVE BEEN',
        'INFORMED OF THE POSSIBILITY OF SUCH DAMAGE.','','',
        '11. GOVERNING LAW','','',
        'These Terms will be governed by the laws of the State of California without regard to conflict of law',
        'principles. To the extent that any lawsuit or court proceeding is permitted hereunder, you and Cloudflare',
        'agree to submit to the personal and exclusive jurisdiction of the state and federal courts located within',
        'San Francisco County, California for the purpose of litigating all such disputes.','','',
        '12. CHANGES TO THESE TERMS','','',
        'Cloudflare reserves the right to make modifications to these Terms at any time. Revised versions of these',
        'Terms will be posted to this Website. Unless otherwise specified, any modifications to the Terms will take',
        'effect the day they are posted to this Website. If you do not agree with the revised Terms, your sole and',
        'exclusive remedy will be to discontinue your use of the Websites and Online Services.','','',
        '13. GENERAL','','',
        'These Terms, together with the Privacy Policy and any other agreements expressly incorporated by reference herein,',
        'constitute the entire and exclusive understanding and agreement between you and Cloudflare regarding your use of',
        'and access to the Websites and Online Services. Use of section headers in these Terms is for convenience only and',
        'will not have any impact on the interpretation of particular provisions. You may not assign or transfer these Terms',
        'or your rights hereunder, in whole or in part, by operation of law or otherwise, without our prior written consent.',
        'We may assign these Terms at any time without notice. The failure to require performance of any provision will not',
        'affect our right to require performance at any time thereafter, nor will a waiver of any breach or default of these',
        'Terms or any provision of these Terms constitute a waiver of any subsequent breach or default or a waiver of the provision',
        'itself. In the event that any part of these Terms is held to be invalid or unenforceable, the unenforceable part will be',
        'given effect to the greatest extent possible and the remaining parts will remain in full force and effect. You acknowledge',
        'that the Websites and Online Services are not intended to be technology protection measures that will help you comply',
        "with the Children’s Online Privacy Protection Act (COPPA) or Children's Internet Protection Act (CIPA).Upon termination",
        'of these Terms, any provision that by its nature or express terms should survive will survive such termination or expiration,',
        'including, but not limited to, Section 2 and Sections 7 through 13.','','',
        '14. CONTACT INFORMATION','','',
        'The Websites and Online Services are operated by Cloudflare, Inc., located at 101 Townsend St., San Francisco,',
        'California 94107. You may contact us by sending correspondence to the foregoing address or by emailing us at',
        'support@cloudflare.com. If you are a California resident, you may have these Terms mailed to you electronically',
        'by sending a letter to the foregoing address with your electronic mail address and a request for these Terms.',''
    ]
    for line in termsAndConditions:
        myList.insert(END, line)
    myList.pack(fill="x")
    scrollView.config(command=myList.yview)
    #argeement check box frame
    argreeCheckBoxFrame = Frame(winRoot, bg="green")
    argreeCheckBoxFrame.pack(fill="x")
    agreeValue = IntVar()
    def checkEffect():
        if agreeValue.get() == 1:
            installButton['state'] = ACTIVE
        else:
            installButton['state'] = DISABLED
   
    agreeMessage = "I have read all the terms and conditions and Ready to install this software."
    termsAndConditionButton = Checkbutton(argreeCheckBoxFrame, text=agreeMessage,variable=agreeValue ,onvalue=1, offvalue=0, command=checkEffect)
    termsAndConditionButton.pack()
 
 

 
    #Install progress bar frame
    installProgressFrame = Frame(winRoot, bg="#FFFFE4")
    installProgressFrame.pack(fill="x")
 
 
 
 
 
    #install and cancel frame
    buttonFrame = Frame(winRoot, bg="#FFFFE4")
    buttonFrame.pack(fill="x", padx=10, pady=[5,0])
    installButton = Button(buttonFrame, text="Install", state=DISABLED)
    installButton.pack(side=LEFT, padx=[20,0])
    cancelButton = Button(buttonFrame, text="Cancel",state=ACTIVE, command=onCloseALL)
    cancelButton.pack(side=RIGHT, padx=[0,20])

    winRoot.mainloop()
#main section----->>>
if realName == 'windows':
    if internetCheckDialogBox():
        mainDialogBox()
    else:
        exit(1)

#planning section---->>>
'''
internet check and if off result no internet on a dialog --done
check box
button install, cancel
progress bar --postponed
github download and configure
cloudflared download and configure


'''