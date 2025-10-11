
┌──(kali㉿kali)-[~]
└─$ john --test                                                                          
Will run 4 OpenMP threads
Benchmarking: descrypt, traditional crypt(3) [DES 256/256 AVX2]... (4xOMP) DONE
Many salts:     37822K c/s real, 9710K c/s virtual
Only one salt:  28925K c/s real, 7474K c/s virtual

Benchmarking: bsdicrypt, BSDI crypt(3) ("_J9..", 725 iterations) [DES 256/256 AVX2]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 725
Many salts:     1070K c/s real, 287021 c/s virtual
Only one salt:  1125K c/s real, 290794 c/s virtual

Benchmarking: md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3]... (4xOMP) DONE
Many salts:     287232 c/s real, 74702 c/s virtual
Only one salt:  295872 c/s real, 75864 c/s virtual

Benchmarking: md5crypt-long, crypt(3) $1$ (and variants) [MD5 32/64]... (4xOMP) DONE
Raw:    26528 c/s real, 7287 c/s virtual

Benchmarking: bcrypt ("$2a$05", 32 iterations) [Blowfish 32/64 X3]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 32
Raw:    4925 c/s real, 1270 c/s virtual

Benchmarking: scrypt (16384, 8, 1) [Salsa20/8 128/128 AVX]... (4xOMP) DONE
Speed for cost 1 (N) of 16384, cost 2 (r) of 8, cost 3 (p) of 1
Raw:    152 c/s real, 40.0 c/s virtual

Benchmarking: LM [DES 256/256 AVX2]... (4xOMP) DONE
Raw:    111501K c/s real, 28516K c/s virtual

Benchmarking: AFS, Kerberos AFS [DES 48/64 4K]... DONE
Short:  495488 c/s real, 485772 c/s virtual
Long:   500096 c/s real, 502609 c/s virtual

Benchmarking: tripcode [DES 256/256 AVX2]... (4xOMP) DONE
Raw:    3887K c/s real, 1008K c/s virtual

Benchmarking: AndroidBackup [PBKDF2-SHA1 256/256 AVX2 8x AES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 10000
Raw:    4352 c/s real, 1145 c/s virtual

Benchmarking: adxcrypt, IBM/Toshiba 4690 [ADXCRYPT 32/64]... (4xOMP) DONE
Raw:    80599K c/s real, 20823K c/s virtual

Benchmarking: agilekeychain, 1Password Agile Keychain [PBKDF2-SHA1 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000
Raw:    83392 c/s real, 21604 c/s virtual

Benchmarking: aix-ssha1, AIX LPA {ssha1} [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 64
Many salts:     1142K c/s real, 294367 c/s virtual
Only one salt:  1137K c/s real, 292050 c/s virtual

Benchmarking: aix-ssha256, AIX LPA {ssha256} [PBKDF2-SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 64
Many salts:     510592 c/s real, 131089 c/s virtual
Only one salt:  420672 c/s real, 115728 c/s virtual

Benchmarking: aix-ssha512, AIX LPA {ssha512} [PBKDF2-SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 64
Many salts:     180448 c/s real, 49034 c/s virtual
Only one salt:  203488 c/s real, 52991 c/s virtual

Benchmarking: andOTP [SHA256 32/64]... (4xOMP) DONE
Raw:    606208 c/s real, 157866 c/s virtual

Benchmarking: ansible, Ansible Vault [PBKDF2-SHA256 HMAC-256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 10000
Raw:    3358 c/s real, 903 c/s virtual

Benchmarking: argon2 [Blake2 AVX]... (4xOMP) DONE
Speed for cost 1 (t) of 3, cost 2 (m) of 4096, cost 3 (p) of 1, cost 4 (type [0:Argon2d 1:Argon2i]) of 0 and 1
Raw:    452 c/s real, 123 c/s virtual

Benchmarking: as400-des, AS/400 DES [DES 32/64]... DONE
Raw:    401763 c/s real, 105173 c/s virtual                                                                                                                                                         
                                                                                                                                                                                                    
Benchmarking: as400-ssha1, AS400-SaltedSHA1 [sha1(utf16be(space_pad_10(uc($s)).$p)) (IBM AS/400 SHA1) 256/256 AVX2 8x1]... DONE                                                                     
Many salts:     14957K c/s real, 15032K c/s virtual                                                                                                                                                 
Only one salt:  12055K c/s real, 12055K c/s virtual                                                                                                                                                 
                                                                                                                                                                                                    
Benchmarking: asa-md5, Cisco ASA [md5($p.$s) (Cisco ASA) 256/256 AVX2 8x3]... DONE                                                                                                                  
Many salts:     28462K c/s real, 28750K c/s virtual                                                                                                                                                 
Only one salt:  16448K c/s real, 16448K c/s virtual                                                                                                                                                 
                                                                                                                                                                                                    
Benchmarking: AxCrypt [PBKDF2-SHA512/SHA1 AES 32/64]... (4xOMP) DONE                                                                                                                                
Speed for cost 1 (iteration count) of 1337 and 60000                                                                                                                                                
Raw:    290 c/s real, 87.0 c/s virtual                                                                                                                                                              
                                                                                                                                                                                                    
Benchmarking: AzureAD [PBKDF2-SHA256 256/256 AVX2 8x]... (4xOMP) DONE                                                                                                                               
Many salts:     309760 c/s real, 83045 c/s virtual                                                                                                                                                  
Only one salt:  310272 c/s real, 81758 c/s virtual                                                                                                                                                  
                                                                                                                                                                                                    
Benchmarking: BestCrypt, Jetico BestCrypt (.jbc) (SHA-256 + AES XTS mode) [PKCS#12 PBE (SHA1/SHA2) 32/64]... (4xOMP) DONE                                                                           
Speed for cost 1 (iteration count) of 16384                                                                                                                                                         
Raw:    571 c/s real, 149 c/s virtual                                                                                                                                                               
                                                                                                                                                                                                    
Benchmarking: BestCryptVE4, BestCrypt Volume Encryption v4 (32768, 16, 1) [scrypt Salsa20/8 128/128 AVX, AES/TwoFish/Serpent/Camellia]... (4xOMP) DONE                                              
Raw:    34.0 c/s real, 10.1 c/s virtual                                                                                                                                                             
                                                                                                                                                                                                    
Benchmarking: bfegg, Eggdrop [Blowfish 32/64]... (4xOMP) DONE
Raw:    131438 c/s real, 33697 c/s virtual

Benchmarking: Bitcoin, Bitcoin Core [SHA512 AES 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 200460
Raw:    147 c/s real, 38.4 c/s virtual

Benchmarking: BitLocker, BitLocker [SHA-256 AES 32/64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1048576
Raw:    10.0 c/s real, 2.6 c/s virtual

Benchmarking: bitshares, BitShares Wallet [SHA-512 64/64]... (4xOMP) DONE
Many salts:     3399K c/s real, 907791 c/s virtual
Only one salt:  3434K c/s real, 919282 c/s virtual

Benchmarking: Bitwarden, Bitwarden Password Manager [PBKDF2-SHA256 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 5000
Raw:    6925 c/s real, 1908 c/s virtual

Benchmarking: BKS, BouncyCastle [PKCS#12 PBE (SHA1) 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    80095 c/s real, 21039 c/s virtual

Benchmarking: Blackberry-ES10 (101x) [SHA-512 256/256 AVX2 4x]... (4xOMP) DONE
Many salts:     292352 c/s real, 75058 c/s virtual
Only one salt:  286464 c/s real, 73926 c/s virtual

Benchmarking: WoWSRP, Battlenet [SHA1 32/64 GMP-exp]... (4xOMP) DONE
Many salts:     449024 c/s real, 116176 c/s virtual
Only one salt:  428032 c/s real, 112640 c/s virtual

Benchmarking: Blockchain, My Wallet (v2 x5000) [PBKDF2-SHA1 AES 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    8819 c/s real, 2281 c/s virtual

Benchmarking: chap, iSCSI CHAP authentication / EAP-MD5 [MD5 32/64]... (4xOMP) DONE
Many salts:     28954K c/s real, 7424K c/s virtual
Only one salt:  16912K c/s real, 4811K c/s virtual

Benchmarking: Clipperz, SRP [SHA256 32/64 GMP-exp]... (4xOMP) DONE
Raw:    176128 c/s real, 51955 c/s virtual

Benchmarking: cloudkeychain, 1Password Cloud Keychain [PBKDF2-SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 40000 and 50000
Raw:    214 c/s real, 73.4 c/s virtual

Benchmarking: dynamic=md5($p) [256/256 AVX2 8x3]... DONE
Raw:    40479K c/s real, 41096K c/s virtual

Benchmarking: cq, ClearQuest [CQWeb]... (4xOMP) DONE
Many salts:     116981K c/s real, 37196K c/s virtual
Only one salt:  35865K c/s real, 11107K c/s virtual

Benchmarking: CRC32 [CRC32 32/64 CRC-32C AVX]... DONE
Speed for cost 1 (version [0:CRC-32 1:CRC-32C]) of 0
Many salts:     124297K c/s real, 126833K c/s virtual
Only one salt:  57266K c/s real, 57266K c/s virtual

Benchmarking: cryptoSafe [AES-256-CBC]... (4xOMP) DONE
Raw:    6399K c/s real, 2153K c/s virtual

Benchmarking: sha1crypt, NetBSD's sha1crypt [PBKDF1-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 20000
Raw:    3820 c/s real, 1086 c/s virtual

Benchmarking: sha256crypt, crypt(3) $5$ (rounds=5000) [SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 5000
Raw:    6053 c/s real, 2125 c/s virtual

Benchmarking: sha512crypt, crypt(3) $6$ (rounds=5000) [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 5000
Raw:    3801 c/s real, 1303 c/s virtual

Benchmarking: Citrix_NS10, Netscaler 10 [SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     27754K c/s real, 9297K c/s virtual
Only one salt:  18144K c/s real, 6028K c/s virtual

Benchmarking: dahua, "MD5 based authentication" Dahua [MD5 32/64]... DONE
Raw:    6527K c/s real, 6527K c/s virtual

Benchmarking: dashlane, Dashlane Password Manager [AES PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    3154 c/s real, 1054 c/s virtual

Benchmarking: diskcryptor, DiskCryptor [PBKDF2-SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000
Raw:    7620 c/s real, 2471 c/s virtual

Benchmarking: Django (x10000) [PBKDF2-SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 10000
Raw:    2624 c/s real, 789 c/s virtual

Benchmarking: django-scrypt [Salsa20/8 128/128 AVX]... (4xOMP) DONE
Speed for cost 1 (N) of 14, cost 2 (r) of 8, cost 3 (p) of 1
Raw:    110 c/s real, 34.1 c/s virtual

Benchmarking: dmd5, DIGEST-MD5 C/R [MD5 32/64]... (4xOMP) DONE
Many salts:     5095K c/s real, 1505K c/s virtual
Only one salt:  2269K c/s real, 803250 c/s virtual

Benchmarking: dmg, Apple DMG [PBKDF2-SHA1 256/256 AVX2 8x 3DES/AES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000, cost 2 (version) of 2 and 1
Raw:    13504 c/s real, 4246 c/s virtual

Benchmarking: dominosec, Lotus Notes/Domino 6 More Secure Internet Password [8/64]... (4xOMP) DONE
Many salts:     913152 c/s real, 259418 c/s virtual
Only one salt:  573504 c/s real, 163858 c/s virtual

Benchmarking: dominosec8, Lotus Notes/Domino 8 [8/64]... (4xOMP) DONE
Raw:    2292 c/s real, 698 c/s virtual

Benchmarking: DPAPImk, DPAPI masterkey file v1 and v2 [SHA1/MD4 PBKDF2-(SHA1/SHA512)-DPAPI-variant 3DES/AES256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 24000
Raw:    1491 c/s real, 420 c/s virtual

Benchmarking: dragonfly3-32, DragonFly BSD $3$ w/ bug, 32-bit [SHA256 32/64]... (4xOMP) DONE
Many salts:     11814K c/s real, 3332K c/s virtual
Only one salt:  10393K c/s real, 2923K c/s virtual

Benchmarking: dragonfly3-64, DragonFly BSD $3$ w/ bug, 64-bit [SHA256 32/64]... (4xOMP) DONE
Many salts:     12765K c/s real, 3565K c/s virtual
Only one salt:  10219K c/s real, 2870K c/s virtual

Benchmarking: dragonfly4-32, DragonFly BSD $4$ w/ bugs, 32-bit [SHA512 64/64]... (4xOMP) DONE
Many salts:     8715K c/s real, 2455K c/s virtual
Only one salt:  8054K c/s real, 2256K c/s virtual

Benchmarking: dragonfly4-64, DragonFly BSD $4$ w/ bugs, 64-bit [SHA512 64/64]... (4xOMP) DONE
Many salts:     8962K c/s real, 2513K c/s virtual
Only one salt:  7880K c/s real, 2210K c/s virtual

Benchmarking: Drupal7, $S$ (x16385) [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 16384
Raw:    1512 c/s real, 428 c/s virtual

Benchmarking: eCryptfs (65536 iterations) [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Raw:    382 c/s real, 114 c/s virtual

Benchmarking: eigrp, EIGRP MD5 / HMAC-SHA-256 authentication [MD5/SHA-256 32/64]... (4xOMP) DONE
Speed for cost 1 (algorithm [2:MD5 3:HMAC-SHA-256]) of 2
Many salts:     12920K c/s real, 3619K c/s virtual
Only one salt:  10813K c/s real, 3028K c/s virtual

Benchmarking: electrum, Electrum Wallet [SHA256 AES / PBKDF2-SHA512 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (kdf [1:SHA256 2:PBKDF2-SHA512]) of 1 and 2
Raw:    13054 c/s real, 3939 c/s virtual

Benchmarking: EncFS [PBKDF2-SHA1 256/256 AVX2 8x AES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 181474
Raw:    156 c/s real, 57.0 c/s virtual

Benchmarking: enpass, Enpass Password Manager [PBKDF2-SHA1/SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (Enpass version) of 5
Raw:    1051 c/s real, 402 c/s virtual

Benchmarking: EPI, EPiServer SID [SHA1 32/64]... (4xOMP) DONE
Many salts:     10182K c/s real, 3505K c/s virtual
Only one salt:  11722K c/s real, 3646K c/s virtual

Benchmarking: EPiServer [SHA1/SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (hash type [1:SHA1 2:SHA256]) of 1
Many salts:     25821K c/s real, 8535K c/s virtual
Only one salt:  45858K c/s real, 13215K c/s virtual

Benchmarking: ethereum, Ethereum Wallet [PBKDF2-SHA256/scrypt Keccak 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 262144, cost 2 (kdf [0:PBKDF2-SHA256 1:scrypt 2:PBKDF2-SHA256 presale]) of 0
Raw:    125 c/s real, 36.5 c/s virtual

Benchmarking: fde, Android FDE [PBKDF2-SHA1 256/256 AVX2 8x SHA256/AES]... (4xOMP) DONE
Raw:    20979 c/s real, 5520 c/s virtual

Benchmarking: Fortigate256, FortiOS256 [SHA256 32/64]... (4xOMP) DONE
Many salts:     16056K c/s real, 4264K c/s virtual
Only one salt:  14274K c/s real, 3751K c/s virtual

Benchmarking: Fortigate, FortiOS [SHA1 32/64]... (4xOMP) DONE
Many salts:     25163K c/s real, 6828K c/s virtual
Only one salt:  24981K c/s real, 6389K c/s virtual

Benchmarking: FormSpring [sha256($s.$p) 256/256 AVX2 8x]... DONE
Many salts:     9898K c/s real, 9948K c/s virtual
Only one salt:  8588K c/s real, 8588K c/s virtual

Benchmarking: FVDE, FileVault 2 [PBKDF2-SHA256 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 41000 and 70400
Raw:    668 c/s real, 171 c/s virtual

Benchmarking: geli, FreeBSD GELI [PBKDF2-SHA512 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 256 and 512
Raw:    35968 c/s real, 9258 c/s virtual

Benchmarking: gost, GOST R 34.11-94 [64/64]... (4xOMP) DONE
Raw:    2058K c/s real, 549596 c/s virtual

Benchmarking: gpg, OpenPGP / GnuPG Secret Key [32/64]... (4xOMP) DONE
Speed for cost 1 (s2k-count) of 65536, cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) of 2, cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) of 3
Raw:    47828 c/s real, 12358 c/s virtual

Benchmarking: HAVAL-128-4 [32/64]... DONE
Raw:    3336K c/s real, 3336K c/s virtual

Benchmarking: HAVAL-256-3 [32/64]... DONE
Raw:    4773K c/s real, 4773K c/s virtual

Benchmarking: hdaa, HTTP Digest access authentication [MD5 256/256 AVX2 8x3]... DONE
Many salts:     8684K c/s real, 8684K c/s virtual
Only one salt:  7787K c/s real, 7826K c/s virtual

Benchmarking: hMailServer [sha256($s.$p) 256/256 AVX2 8x]... DONE
Many salts:     9947K c/s real, 9947K c/s virtual
Only one salt:  8606K c/s real, 8649K c/s virtual

Benchmarking: hsrp, "MD5 authentication" HSRP, HSRPv2, VRRP, GLBP [MD5 32/64]... (4xOMP) DONE
Many salts:     17842K c/s real, 4557K c/s virtual
Only one salt:  10625K c/s real, 2710K c/s virtual

Benchmarking: IKE, PSK [HMAC MD5/SHA1 32/64]... (4xOMP) DONE
Speed for cost 1 (hash algorithm used for hmac [1:MD5 2:SHA1]) of 1 and 2
Raw:    3000K c/s real, 770300 c/s virtual

Benchmarking: ipb2, Invision Power Board 2.x [MD5 256/256 AVX2 8x3]... (4xOMP) DONE
Many salts:     48955K c/s real, 12584K c/s virtual
Only one salt:  28016K c/s real, 7572K c/s virtual

Benchmarking: itunes-backup, Apple iTunes Backup [PBKDF2-SHA1 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (version) of 9 and 10, cost 2 (iteration count) of 10000
Raw:    3621 c/s real, 1012 c/s virtual

Benchmarking: iwork, Apple iWork '09 or newer [PBKDF2-SHA1 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 100000
Raw:    760 c/s real, 224 c/s virtual

Benchmarking: KeePass [SHA256 AES 32/64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 50000 and 6000, cost 2 (version) of 1 and 2, cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) of 0
Raw:    421 c/s real, 112 c/s virtual

Benchmarking: keychain, Mac OS X Keychain [PBKDF2-SHA1 3DES 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    38973 c/s real, 10361 c/s virtual

Benchmarking: keyring, GNOME Keyring [SHA256 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 3221
Raw:    21082 c/s real, 5780 c/s virtual

Benchmarking: keystore, Java KeyStore [SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Warning: "Many salts" test limited: 37/256
Many salts:     4825K c/s real, 1277K c/s virtual
Only one salt:  4564K c/s real, 1221K c/s virtual

Benchmarking: known_hosts, HashKnownHosts HMAC-SHA1 [SHA1 32/64]... (4xOMP) DONE
Many salts:     14374K c/s real, 3833K c/s virtual
Only one salt:  12347K c/s real, 3319K c/s virtual

Benchmarking: krb4, Kerberos v4 TGT [DES 32/64]... DONE
Short:  299431 c/s real, 295006 c/s virtual
Long:   299116 c/s real, 299116 c/s virtual

Benchmarking: krb5, Kerberos v5 TGT [3DES 32/64]... DONE
Raw:    77027 c/s real, 77414 c/s virtual

Benchmarking: krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     1573K c/s real, 419144 c/s virtual
Only one salt:  1434K c/s real, 365975 c/s virtual

Benchmarking: krb5pa-sha1, Kerberos 5 AS-REQ Pre-Auth etype 17/18 [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    10778 c/s real, 2781 c/s virtual

Benchmarking: krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4]... (4xOMP) DONE
Many salts:     3485K c/s real, 897087 c/s virtual
Only one salt:  2266K c/s real, 584181 c/s virtual

Benchmarking: krb5-17, Kerberos 5 DB etype 17 [DES / PBKDF2-SHA1 256/256 AVX2 8x AES]... (4xOMP) DONE
Raw:    21463 c/s real, 5656 c/s virtual

Benchmarking: krb5-18, Kerberos 5 DB etype 18 [DES / PBKDF2-SHA1 256/256 AVX2 8x AES]... (4xOMP) DONE
Raw:    10826 c/s real, 2857 c/s virtual

Benchmarking: krb5-3, Kerberos 5 DB etype 3 [DES / PBKDF2-SHA1 256/256 AVX2 8x AES]... (4xOMP) DONE
Many salts:     5881K c/s real, 1510K c/s virtual
Only one salt:  4870K c/s real, 1274K c/s virtual

Benchmarking: kwallet, KDE KWallet [SHA1 / PBKDF2-SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Raw:    14901 c/s real, 3930 c/s virtual

Benchmarking: lp, LastPass offline [PBKDF2-SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 500
Many salts:     72960 c/s real, 18683 c/s virtual
Only one salt:  69120 c/s real, 18070 c/s virtual

Benchmarking: lpcli, LastPass CLI [PBKDF2-SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1234
Many salts:     25872 c/s real, 6926 c/s virtual
Only one salt:  27264 c/s real, 7174 c/s virtual

Benchmarking: leet [SHA-512(256/256 AVX2 4x) + Whirlpool(OpenSSL/64)]... (4xOMP) DONE
Warning: "Many salts" test limited: 87/256
Many salts:     5701K c/s real, 1524K c/s virtual
Only one salt:  4695K c/s real, 1336K c/s virtual

Benchmarking: lotus5, Lotus Notes/Domino 5 [8/64 X3]... (4xOMP) DONE
Raw:    2354K c/s real, 610456 c/s virtual

Benchmarking: lotus85, Lotus Notes/Domino 8.5 [8/64]... (4xOMP) DONE
Many salts:     543872 c/s real, 139454 c/s virtual
Only one salt:  442332 c/s real, 119180 c/s virtual

Benchmarking: LUKS [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    216 c/s real, 56.9 c/s virtual

Benchmarking: MD2 [MD2 32/64]... (4xOMP) DONE
Raw:    857856 c/s real, 228153 c/s virtual

Benchmarking: mdc2, MDC-2 [MDC-2DES]... (4xOMP) DONE
Raw:    6541K c/s real, 1721K c/s virtual

Benchmarking: MediaWiki [md5($s.md5($p)) 256/256 AVX2 8x3]... DONE
Many salts:     34409K c/s real, 34409K c/s virtual
Only one salt:  14340K c/s real, 14340K c/s virtual

Benchmarking: monero, monero Wallet [Pseudo-AES / ChaCha / Various 32/64]... (4xOMP) DONE
Raw:    8.0 c/s real, 2.4 c/s virtual

Benchmarking: money, Microsoft Money (2002 to Money Plus) [MD5/SHA1 32/64]... (4xOMP) DONE
Many salts:     2592K c/s real, 788216 c/s virtual
Only one salt:  2426K c/s real, 719075 c/s virtual

Benchmarking: MongoDB, system / network [MD5 32/64]... (4xOMP) DONE
Speed for cost 1 (salt type) of 0 and 1
Raw:    6488K c/s real, 2333K c/s virtual

Benchmarking: scram [SCRAM PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    5251 c/s real, 2111 c/s virtual

Benchmarking: Mozilla, Mozilla key3.db [SHA1 3DES 32/64]... (4xOMP) DONE
Many salts:     614912 c/s real, 207390 c/s virtual
Only one salt:  715264 c/s real, 237629 c/s virtual

Benchmarking: mscash, MS Cache Hash (DCC) [MD4 32/64]... (4xOMP) DONE
Many salts:     37343K c/s real, 11761K c/s virtual
Only one salt:  12621K c/s real, 3895K c/s virtual

Benchmarking: mscash2, MS Cache Hash 2 (DCC2) [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    6750 c/s real, 1921 c/s virtual

Benchmarking: MSCHAPv2, C/R [MD4 DES (ESS MD5) 256/256 AVX2 8x3]... DONE
Many salts:     10033M c/s real, 10134M c/s virtual
Only one salt:  54362K c/s real, 54636K c/s virtual

Benchmarking: mschapv2-naive, MSCHAPv2 C/R [MD4 DES 256/256 AVX2 naive]... (4xOMP) DONE
Many salts:     268566K c/s real, 84058K c/s virtual
Only one salt:  15495K c/s real, 4524K c/s virtual

Benchmarking: krb5pa-md5, Kerberos 5 AS-REQ Pre-Auth etype 23 [32/64]... (4xOMP) DONE
Many salts:     2139K c/s real, 626469 c/s virtual
Only one salt:  1086K c/s real, 331278 c/s virtual

Benchmarking: mssql, MS SQL [SHA1 256/256 AVX2 8x]... DONE
Many salts:     33234K c/s real, 33401K c/s virtual
Only one salt:  16165K c/s real, 16165K c/s virtual

Benchmarking: mssql05, MS SQL 2005 [SHA1 256/256 AVX2 8x]... DONE
Many salts:     38007K c/s real, 38007K c/s virtual
Only one salt:  25809K c/s real, 25809K c/s virtual

Benchmarking: mssql12, MS SQL 2012/2014 [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Many salts:     24135K c/s real, 6427K c/s virtual
Only one salt:  13467K c/s real, 3735K c/s virtual

Benchmarking: multibit, MultiBit Wallet [MD5/scrypt AES 32/64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 3, cost 2 (kdf [1:MD5 2:scrypt hd 3:scrypt classic]) of 1
Many salts:     1988K c/s real, 558467 c/s virtual
Only one salt:  1659K c/s real, 478204 c/s virtual

Benchmarking: mysqlna, MySQL Network Authentication [SHA1 32/64]... (4xOMP) DONE
Many salts:     8418K c/s real, 2328K c/s virtual
Only one salt:  9121K c/s real, 2422K c/s virtual

Benchmarking: mysql-sha1, MySQL 4.1+ [SHA1 256/256 AVX2 8x]... DONE
Raw:    15839K c/s real, 16163K c/s virtual

Benchmarking: mysql, MySQL pre-4.1 [32/64]... DONE
Raw:    49616K c/s real, 49866K c/s virtual

Benchmarking: net-ah, IPsec AH HMAC-MD5-96 [MD5 32/64]... (4xOMP) DONE
Many salts:     2282K c/s real, 785534 c/s virtual                                                                                                                                                  
Only one salt:  4311K c/s real, 1277K c/s virtual                                                                                                                                                   
                                                                                                                                                                                                    
Benchmarking: nethalflm, HalfLM C/R [DES 32/64]... (4xOMP) DONE                                                                                                                                     
Many salts:     13877K c/s real, 3745K c/s virtual                                                                                                                                                  
Only one salt:  2551K c/s real, 703947 c/s virtual                                                                                                                                                  
                                                                                                                                                                                                    
Benchmarking: netlm, LM C/R [DES 32/64]... (4xOMP) DONE                                                                                                                                             
Warning: "Many salts" test limited: 63/256                                                                                                                                                          
Many salts:     16432K c/s real, 4223K c/s virtual                                                                                                                                                  
Only one salt:  1772K c/s real, 1235K c/s virtual                                                                                                                                                   
                                                                                                                                                                                                    
Benchmarking: netlmv2, LMv2 C/R [MD4 HMAC-MD5 32/64]... (4xOMP) DONE                                                                                                                                
Many salts:     4930K c/s real, 1270K c/s virtual                                                                                                                                                   
Only one salt:  3607K c/s real, 941986 c/s virtual                                                                                                                                                  
                                                                                                                                                                                                    
Benchmarking: net-md5, "Keyed MD5" RIPv2, OSPF, BGP, SNMPv2 [MD5 32/64]... (4xOMP) DONE                                                                                                             
Many salts:     12909K c/s real, 12718K c/s virtual                                                                                                                                                 
Only one salt:  10395K c/s real, 10448K c/s virtual                                                                                                                                                 
                                                                                                                                                                                                    
Benchmarking: netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64]... (4xOMP) DONE                                                                                                                            
Many salts:     4308K c/s real, 1123K c/s virtual                                                                                                                                                   
Only one salt:  3445K c/s real, 891529 c/s virtual                                                                                                                                                  
                                                                                                                                                                                                    
Benchmarking: netntlm, NTLMv1 C/R [MD4 DES (ESS MD5) 256/256 AVX2 8x3]... DONE                                                                                                                      
Many salts:     12467M c/s real, 12467M c/s virtual                                                                                                                                                 
Only one salt:  69601K c/s real, 69601K c/s virtual                                                                                                                                                 

Benchmarking: netntlm-naive, NTLMv1 C/R [MD4 DES (ESS MD5) DES 256/256 AVX2 naive]... (4xOMP) DONE
Many salts:     613638K c/s real, 156940K c/s virtual
Only one salt:  24834K c/s real, 6442K c/s virtual

Benchmarking: net-sha1, "Keyed SHA1" BFD [SHA1 32/64]... (4xOMP) DONE
Many salts:     13628K c/s real, 13493K c/s virtual
Only one salt:  10622K c/s real, 10622K c/s virtual

Benchmarking: nk, Nuked-Klan CMS [SHA1 MD5 32/64]... (4xOMP) DONE
Warning: "Many salts" test limited: 153/256
Many salts:     10027K c/s real, 2597K c/s virtual
Only one salt:  9520K c/s real, 2450K c/s virtual

Benchmarking: notes, Apple Notes [PBKDF2-SHA256 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 20000
Raw:    1900 c/s real, 488 c/s virtual

Benchmarking: md5ns, Netscreen [md5($s.$p) (OSC) (PW > 31 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     22369K c/s real, 22369K c/s virtual
Only one salt:  15719K c/s real, 15641K c/s virtual

Benchmarking: nsec3, DNSSEC NSEC3 [32/64]... DONE
Raw:    87800 c/s real, 88241 c/s virtual

Benchmarking: NT [MD4 256/256 AVX2 8x3]... DONE
Raw:    67461K c/s real, 67461K c/s virtual

Benchmarking: o10glogon, Oracle 10g-logon protocol [DES-AES128-MD5 32/64]... (4xOMP) DONE
Many salts:     1139K c/s real, 310832 c/s virtual
Only one salt:  1279K c/s real, 342567 c/s virtual

Benchmarking: o3logon, Oracle O3LOGON protocol [SHA1 DES 32/64]... (4xOMP) DONE
Warning: "Many salts" test limited: 59/256
Many salts:     966656 c/s real, 259853 c/s virtual
Only one salt:  945544 c/s real, 256483 c/s virtual

Benchmarking: o5logon, Oracle O5LOGON protocol [SHA1 AES 32/64]... (4xOMP) DONE
Many salts:     6610K c/s real, 1954K c/s virtual
Only one salt:  8126K c/s real, 2217K c/s virtual

Benchmarking: ODF, OpenDocument Star/Libre/OpenOffice [PBKDF2-SHA1 256/256 AVX2 8x BF/AES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1024, cost 2 (crypto [0=Blowfish 1=AES]) of 0 and 1
Raw:    33440 c/s real, 9050 c/s virtual

Benchmarking: Office, 2007/2010/2013 [SHA1 256/256 AVX2 8x / SHA512 256/256 AVX2 4x AES]... (4xOMP) DONE
Speed for cost 1 (MS Office version) of 2007, cost 2 (iteration count) of 50000
Raw:    2106 c/s real, 652 c/s virtual

Benchmarking: oldoffice, MS Office <= 2003 [MD5/SHA1 RC4 32/64]... (4xOMP) DONE
Speed for cost 1 (hash type [0-1:MD5+RC4-40 3:SHA1+RC4-40 4:SHA1+RC4-128 5:SHA1+RC4-56]) of 1 and 0
Many salts:     1067K c/s real, 338732 c/s virtual
Only one salt:  780288 c/s real, 257520 c/s virtual

Benchmarking: OpenBSD-SoftRAID [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (kdf) of 1, cost 2 (iteration count) of 8192
Raw:    3884 c/s real, 1102 c/s virtual

Benchmarking: openssl-enc, OpenSSL "enc" encryption (AES-128, MD5) [32/64]... (4xOMP) DONE
Many salts:     3301K c/s real, 1024K c/s virtual
Only one salt:  3370K c/s real, 1007K c/s virtual

Benchmarking: oracle, Oracle 10 [DES 32/64]... (4xOMP) DONE
Many salts:     2665K c/s real, 776459 c/s virtual
Only one salt:  1720K c/s real, 535925 c/s virtual

Benchmarking: oracle11, Oracle 11g [SHA1 256/256 AVX2 8x]... DONE
Many salts:     37243K c/s real, 37619K c/s virtual
Only one salt:  21600K c/s real, 21818K c/s virtual

Benchmarking: Oracle12C [PBKDF2-SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Raw:    2897 c/s real, 836 c/s virtual

Benchmarking: osc, osCommerce [md5($s.$p) (OSC) 256/256 AVX2 8x3]... DONE
Many salts:     24301K c/s real, 24423K c/s virtual
Only one salt:  18170K c/s real, 18170K c/s virtual

Benchmarking: ospf, OSPF / IS-IS [HMAC-SHA-X 32/64]... (4xOMP) DONE
Raw:    4849K c/s real, 1451K c/s virtual

Benchmarking: Padlock [PBKDF2-SHA256 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 10000
Raw:    3137 c/s real, 903 c/s virtual

Benchmarking: Palshop, MD5(Palshop) [MD5 + SHA1 32/64]... (4xOMP) DONE
Raw:    7662K c/s real, 2124K c/s virtual

Benchmarking: Panama [Panama 32/64]... (4xOMP) DONE
Raw:    2748K c/s real, 805987 c/s virtual

Benchmarking: PBKDF2-HMAC-MD4 [PBKDF2-MD4 256/256 AVX2 8x3]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000
Raw:    239616 c/s real, 64499 c/s virtual

Benchmarking: PBKDF2-HMAC-MD5 [PBKDF2-MD5 256/256 AVX2 8x3]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000
Raw:    142901 c/s real, 39239 c/s virtual

Benchmarking: PBKDF2-HMAC-SHA1 [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000
Raw:    69504 c/s real, 19333 c/s virtual

Benchmarking: PBKDF2-HMAC-SHA256 [PBKDF2-SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000
Raw:    28401 c/s real, 8109 c/s virtual

Benchmarking: PBKDF2-HMAC-SHA512, GRUB2 / OS X 10.8+ [PBKDF2-SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000
Raw:    12664 c/s real, 3436 c/s virtual

Benchmarking: PDF [MD5 SHA2 RC4/AES 32/64]... (4xOMP) DONE
Speed for cost 1 (revision) of 4
Raw:    126464 c/s real, 37195 c/s virtual

Benchmarking: PEM, PKCS#8 private key (RSA/DSA/ECDSA) [PBKDF2-SHA1 256/256 AVX2 8x 3DES/AES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 4096, cost 2 (cipher [1=3DES 2/3/4=AES-128/192/256]) of 1
Raw:    9885 c/s real, 3578 c/s virtual

Benchmarking: pfx, (.pfx, .p12) [PKCS#12 PBE (SHA1/SHA2) 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 2048, cost 2 (mac-type [1:SHA1 224:SHA224 256:SHA256 384:SHA384 512:SHA512]) of 1
Raw:    35152 c/s real, 14302 c/s virtual

Benchmarking: pgpdisk, PGP Disk / Virtual Disk [SHA1 64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 16000, cost 2 (algorithm [3=CAST 4=TwoFish 5/6/7=AES]) of 5
Raw:    2774 c/s real, 780 c/s virtual

Benchmarking: pgpsda, PGP Self Decrypting Archive [SHA1 64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 16000
Raw:    6743 c/s real, 2156 c/s virtual

Benchmarking: pgpwde, PGP Whole Disk Encryption [S2K-SHA1 64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 131072
Raw:    4452 c/s real, 1619 c/s virtual

Benchmarking: phpass ($P$9) [phpass ($P$ or $H$) 256/256 AVX2 8x3]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 2048
Many salts:     95331 c/s real, 29570 c/s virtual
Only one salt:  56064 c/s real, 20424 c/s virtual

Benchmarking: PHPS [md5(md5($p).$s) 256/256 AVX2 8x3]... DONE
Many salts:     39483K c/s real, 39882K c/s virtual
Only one salt:  12961K c/s real, 13092K c/s virtual

Benchmarking: PHPS2 [md5(md5($p).$s) 256/256 AVX2 8x3]... DONE
Many salts:     37428K c/s real, 37998K c/s virtual
Only one salt:  12487K c/s real, 12487K c/s virtual

Benchmarking: pix-md5, Cisco PIX [md5($p) (Cisco PIX) 256/256 AVX2 8x3]... DONE
Raw:    22123K c/s real, 22123K c/s virtual

Benchmarking: PKZIP [32/64]... (4xOMP) DONE
Many salts:     18857K c/s real, 6349K c/s virtual
Only one salt:  19477K c/s real, 5506K c/s virtual

Benchmarking: po, Post.Office [MD5 32/64]... DONE
Many salts:     4656K c/s real, 4656K c/s virtual
Only one salt:  3987K c/s real, 4007K c/s virtual

Benchmarking: postgres, PostgreSQL C/R [MD5 32/64]... (4xOMP) DONE
Many salts:     7801K c/s real, 2360K c/s virtual
Only one salt:  8002K c/s real, 2364K c/s virtual

Benchmarking: PST, custom CRC-32 [32/64]... DONE
Raw:    77043K c/s real, 77043K c/s virtual

Benchmarking: PuTTY, Private Key (RSA/DSA/ECDSA/ED25519) [SHA1/AES 32/64]... (4xOMP) DONE
Raw:    697536 c/s real, 205397 c/s virtual

Benchmarking: pwsafe, Password Safe [SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 2048
Raw:    29257 c/s real, 8943 c/s virtual

Benchmarking: qnx, qnx hash (rounds=1000) [QNX 32/64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 1000, cost 2 (algorithm [5:MD5 256:SHA256 512:SHA512]) of 5
Raw:    152079 c/s real, 47044 c/s virtual

Benchmarking: RACF [DES 32/64]... (4xOMP) DONE
Many salts:     23904K c/s real, 6781K c/s virtual
Only one salt:  6799K c/s real, 2144K c/s virtual

Benchmarking: RACF-KDFAES [KDFAES (DES + HMAC-SHA256/64 + AES-256)]... (4xOMP) DONE
Warning: "Many salts" test limited: 2/256
Many salts:     0.5 c/s real, 0.2 c/s virtual
Only one salt:  0.3 c/s real, 0.1 c/s virtual

Benchmarking: radius, RADIUS authentication [MD5 32/64]... (4xOMP) DONE
Many salts:     13043K c/s real, 4032K c/s virtual
Only one salt:  6806K c/s real, 2346K c/s virtual

Benchmarking: RAdmin, v2.x [MD5 32/64]... (4xOMP) DONE
Raw:    12458K c/s real, 4032K c/s virtual

Benchmarking: RAKP, IPMI 2.0 RAKP (RMCP+) [HMAC-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     31522K c/s real, 9466K c/s virtual
Only one salt:  14024K c/s real, 3715K c/s virtual

Benchmarking: rar, RAR3 (length 5) [SHA1 256/256 AVX2 8x AES]... (4xOMP) DONE
Raw:    434 c/s real, 113 c/s virtual

Benchmarking: RAR5 [PBKDF2-SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 32768
Raw:    975 c/s real, 284 c/s virtual

Benchmarking: Raw-SHA512 [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Raw:    14786K c/s real, 4147K c/s virtual

Benchmarking: Raw-Blake2 [BLAKE2b 512 128/128 AVX]... (4xOMP) DONE
Raw:    12650K c/s real, 3502K c/s virtual

Benchmarking: Raw-Keccak [Keccak 512 32/64]... (4xOMP) DONE
Raw:    5547K c/s real, 1537K c/s virtual

Benchmarking: Raw-Keccak-256 [Keccak 256 32/64]... (4xOMP) DONE
Raw:    6070K c/s real, 1605K c/s virtual

Benchmarking: Raw-MD4 [MD4 256/256 AVX2 8x3]... DONE
Raw:    64427K c/s real, 64750K c/s virtual

Benchmarking: Raw-MD5 [MD5 256/256 AVX2 8x3]... DONE
Raw:    53366K c/s real, 53366K c/s virtual

Benchmarking: Raw-MD5u [md5(utf16($p)) 256/256 AVX2 8x3]... DONE
Raw:    50896K c/s real, 50896K c/s virtual

Benchmarking: Raw-SHA1 [SHA1 256/256 AVX2 8x]... DONE
Raw:    31755K c/s real, 31755K c/s virtual

Benchmarking: Raw-SHA1-AxCrypt [SHA1 256/256 AVX2 8x]... DONE
Raw:    31410K c/s real, 31410K c/s virtual

Benchmarking: Raw-SHA1-Linkedin [SHA1 256/256 AVX2 8x]... DONE
Raw:    30867K c/s real, 30867K c/s virtual

Benchmarking: Raw-SHA224 [SHA224 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    40385K c/s real, 10340K c/s virtual

Benchmarking: Raw-SHA256 [SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    42958K c/s real, 10917K c/s virtual

Benchmarking: Raw-SHA3 [SHA3 512 32/64]... (4xOMP) DONE
Raw:    6749K c/s real, 1719K c/s virtual

Benchmarking: Raw-SHA384 [SHA384 256/256 AVX2 4x]... (4xOMP) DONE
Raw:    22339K c/s real, 5677K c/s virtual

Benchmarking: restic, Restic Repository [scrypt Salsa20/8 128/128 AVX, Poly1305]... (4xOMP) DONE
Speed for cost 1 (N) of 8192, cost 2 (r) of 8, cost 3 (p) of 1
Raw:    312 c/s real, 81.1 c/s virtual

Benchmarking: ripemd-128, RIPEMD 128 [32/64]... DONE
Raw:    7549K c/s real, 7549K c/s virtual

Benchmarking: ripemd-160, RIPEMD 160 [32/64]... DONE
Raw:    4873K c/s real, 4873K c/s virtual

Benchmarking: rsvp, HMAC-MD5 / HMAC-SHA1, RSVP, IS-IS, OMAPI, RNDC, TSIG [MD5 32/64]... (4xOMP) DONE
Speed for cost 1 (hash algorithm used for hmac [1:MD5 2:SHA1 3:SHA224 4:SHA256 5:SHA384 6:SHA512]) of 1 and 2
Many salts:     9467K c/s real, 2427K c/s virtual
Only one salt:  5715K c/s real, 1441K c/s virtual

Benchmarking: RVARY [DES 32/64]... (4xOMP) DONE
Raw:    13350K c/s real, 3371K c/s virtual

Benchmarking: Siemens-S7 [HMAC-SHA1 32/64]... (4xOMP) DONE
Many salts:     13467K c/s real, 3654K c/s virtual
Only one salt:  6747K c/s real, 1703K c/s virtual

Benchmarking: Salted-SHA1 [SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     91422K c/s real, 24775K c/s virtual
Only one salt:  53297K c/s real, 13510K c/s virtual

Benchmarking: SSHA512, LDAP [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Many salts:     26378K c/s real, 6694K c/s virtual
Only one salt:  19333K c/s real, 4925K c/s virtual

Benchmarking: sapb, SAP CODVN B (BCODE) [MD5 256/256 AVX2 8x3]... (4xOMP) DONE
Many salts:     37699K c/s real, 9617K c/s virtual
Only one salt:  27770K c/s real, 7048K c/s virtual

Benchmarking: sapg, SAP CODVN F/G (PASSCODE) [SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     23580K c/s real, 6077K c/s virtual
Only one salt:  19304K c/s real, 4887K c/s virtual

Benchmarking: saph, SAP CODVN H (PWDSALTEDHASH) (SHA1x1024) [SHA-1/SHA-2 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (hash type [1:SHA1 2:SHA256 3:SHA384 4:SHA512]) of 1, cost 2 (iteration count) of 1024
Many salts:     146977 c/s real, 37395 c/s virtual
Only one salt:  131072 c/s real, 34267 c/s virtual

Benchmarking: sappse, SAP PSE [PKCS#12 PBE (SHA1) 256/256 AVX2 8x 3DES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 2048
Raw:    29166 c/s real, 7430 c/s virtual

Benchmarking: securezip, PKWARE SecureZIP [SHA1 AES 32/64]... (4xOMP) DONE
Many salts:     1521K c/s real, 386209 c/s virtual
Only one salt:  1421K c/s real, 360281 c/s virtual

Benchmarking: 7z, 7-Zip archive encryption (512K iterations) [SHA256 256/256 AVX2 8x AES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 524288, cost 2 (padding size) of 4, cost 3 (compression type) of 128, cost 4 (data length) of 108
Raw:    150 c/s real, 38.8 c/s virtual

Benchmarking: Signal, Signal Android [PKCS#12 PBE (SHA1) 32/64]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 6024 and 6097
Raw:    5910 c/s real, 1511 c/s virtual

Benchmarking: SIP [MD5 32/64]... (4xOMP) DONE
Warning: "Many salts" test limited: 176/256
Many salts:     11476K c/s real, 2927K c/s virtual
Only one salt:  9651K c/s real, 2559K c/s virtual

Benchmarking: skein-256, Skein 256 [Skein 32/64]... (4xOMP) DONE
Raw:    9549K c/s real, 2660K c/s virtual

Benchmarking: skein-512, Skein 512 [Skein 32/64]... (4xOMP) DONE
Raw:    4825K c/s real, 1595K c/s virtual

Benchmarking: skey, S/Key [MD4/MD5/SHA1/RMD160 32/64]... DONE
Speed for cost 1 (hash type [1:MD4 2:MD5 3:SHA1 4:RMD160]) of 1 and 2, cost 2 (iteration count) of 96 and 99
Raw:    104369 c/s real, 104369 c/s virtual

Benchmarking: SL3, Nokia operator unlock [SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     93217K c/s real, 25951K c/s virtual
Only one salt:  43515K c/s real, 11682K c/s virtual

Benchmarking: Snefru-128 [32/64]... (4xOMP) DONE
Raw:    1463K c/s real, 383563 c/s virtual

Benchmarking: Snefru-256 [32/64]... (4xOMP) DONE
Raw:    1049K c/s real, 303791 c/s virtual

Benchmarking: LastPass, sniffed sessions [PBKDF2-SHA256 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 500
Warning: "Many salts" test limited: 134/256
Many salts:     68266 c/s real, 18031 c/s virtual
Only one salt:  67757 c/s real, 17920 c/s virtual

Benchmarking: SNMP, SNMPv3 USM [HMAC-MD5-96/HMAC-SHA1-96 32/64]... (4xOMP) DONE
Raw:    902 c/s real, 252 c/s virtual

Benchmarking: solarwinds, SolarWinds Orion [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    1257 c/s real, 373 c/s virtual

Benchmarking: SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64]... (4xOMP) DONE
Speed for cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) of 0 and 1, cost 2 (iteration count) of 1 and 2
Raw:    2675K c/s real, 696845 c/s virtual

Benchmarking: sspr, NetIQ SSPR / Adobe AEM [MD5/SHA1/SHA256/SHA512 32/64]... (4xOMP) DONE
Speed for cost 1 (KDF [0:MD5 1:SHA1 2:SHA1_SALT 3:SHA256_SALT 4:SHA512_SALT]) of 1, cost 2 (iteration count) of 100000
Raw:    304 c/s real, 87.2 c/s virtual

Benchmarking: Stribog-256 [GOST R 34.11-2012 128/128 AVX 1x]... (4xOMP) DONE
Raw:    1832K c/s real, 479205 c/s virtual

Benchmarking: Stribog-512 [GOST R 34.11-2012 128/128 AVX 1x]... (4xOMP) DONE
Raw:    1929K c/s real, 495942 c/s virtual

Benchmarking: STRIP, Password Manager [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    9170 c/s real, 2644 c/s virtual

Benchmarking: SunMD5 [MD5 256/256 AVX2 8x3]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 5000
Raw:    3428 c/s real, 886 c/s virtual

Benchmarking: SybaseASE, Sybase ASE [SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     23166K c/s real, 6136K c/s virtual
Only one salt:  6045K c/s real, 1584K c/s virtual

Benchmarking: Sybase-PROP [salted FEAL-8 32/64]... (4xOMP) DONE
Many salts:     2724K c/s real, 731507 c/s virtual
Only one salt:  2117K c/s real, 614697 c/s virtual

Benchmarking: tacacs-plus, TACACS+ [MD5 32/64]... (4xOMP) DONE
Many salts:     27284K c/s real, 7189K c/s virtual
Only one salt:  20804K c/s real, 5496K c/s virtual

Benchmarking: tcp-md5, TCP MD5 Signatures, BGP, MSDP [MD5 32/64]... (4xOMP) DONE
Many salts:     29962K c/s real, 7853K c/s virtual
Only one salt:  17137K c/s real, 4544K c/s virtual

Benchmarking: telegram [PBKDF2-SHA1/SHA512 256/256 AVX2 8x AES]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 4000
Raw:    2512 c/s real, 719 c/s virtual

Benchmarking: tezos, Tezos Key [PBKDF2-SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 2048
Raw:    5120 c/s real, 1537 c/s virtual

Benchmarking: Tiger [Tiger 32/64]... (4xOMP) DONE
Raw:    19963K c/s real, 5302K c/s virtual

Benchmarking: tc_aes_xts, TrueCrypt AES256_XTS [SHA512/RIPEMD160/WHIRLPOOL 256/256 AVX2 4x]... (4xOMP) DONE
Speed for cost 1 (hash algorithm [1:SHA512 2:RIPEMD160 3:Whirlpool]) of 1
Raw:    12106 c/s real, 3399 c/s virtual

Benchmarking: tc_ripemd160, TrueCrypt AES256_XTS [RIPEMD160 32/64]... (4xOMP) DONE
Raw:    1047 c/s real, 293 c/s virtual

Benchmarking: tc_ripemd160boot, TrueCrypt AES/Twofish/Serpent [RIPEMD160 32/64]... (4xOMP) DONE
Raw:    2236 c/s real, 581 c/s virtual

Benchmarking: tc_sha512, TrueCrypt AES256_XTS [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Raw:    13619 c/s real, 3558 c/s virtual

Benchmarking: tc_whirlpool, TrueCrypt AES256_XTS [WHIRLPOOL 32/64]... (4xOMP) DONE
Raw:    2292 c/s real, 593 c/s virtual

Benchmarking: vdi, VirtualBox-VDI AES_XTS [PBKDF2-SHA256 256/256 AVX2 8x + AES_XTS]... (4xOMP) DONE
Raw:    6106 c/s real, 1623 c/s virtual

Benchmarking: OpenVMS, Purdy [32/64]... (4xOMP) DONE
Many salts:     5296K c/s real, 1368K c/s virtual
Only one salt:  4977K c/s real, 1287K c/s virtual

Benchmarking: vmx, VMware VMX [PBKDF2-SHA1 AES 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 10000
Raw:    4234 c/s real, 1106 c/s virtual

Benchmarking: VNC [DES 32/64]... (4xOMP) DONE
Many salts:     14893K c/s real, 4003K c/s virtual
Only one salt:  8093K c/s real, 2456K c/s virtual

Benchmarking: vtp, "MD5 based authentication" VTP [MD5 32/64]... (4xOMP) DONE
Many salts:     2598K c/s real, 766640 c/s virtual
Only one salt:  19320 c/s real, 6187 c/s virtual

Benchmarking: wbb3, WoltLab BB3 [SHA1 32/64]... (4xOMP) DONE
Many salts:     6345K c/s real, 1795K c/s virtual
Only one salt:  4706K c/s real, 1337K c/s virtual

Benchmarking: whirlpool [WHIRLPOOL 32/64]... (4xOMP) DONE
Raw:    5554K c/s real, 1589K c/s virtual

Benchmarking: whirlpool0 [WHIRLPOOL-0 32/64]... (4xOMP) DONE
Raw:    5465K c/s real, 1576K c/s virtual

Benchmarking: whirlpool1 [WHIRLPOOL-1 32/64]... (4xOMP) DONE
Raw:    3859K c/s real, 1165K c/s virtual

Benchmarking: wpapsk, WPA/WPA2/PMF/PMKID PSK [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    10889 c/s real, 2777 c/s virtual

Benchmarking: wpapsk-pmk, WPA/WPA2/PMF/PMKID master key [MD5/SHA-1/SHA-2]... (4xOMP) DONE
Raw:    3349K c/s real, 862163 c/s virtual

Benchmarking: xmpp-scram [XMPP SCRAM PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Raw:    22195 c/s real, 5624 c/s virtual

Benchmarking: xsha, Mac OS X 10.4 - 10.6 [SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     138516K c/s real, 35067K c/s virtual
Only one salt:  57083K c/s real, 14488K c/s virtual

Benchmarking: xsha512, Mac OS X 10.7 [SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Many salts:     26738K c/s real, 6769K c/s virtual
Only one salt:  20447K c/s real, 5189K c/s virtual

Benchmarking: zed, Prim'X Zed! encrypted archives [PKCS#12 PBE (SHA1/SHA256) 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (iteration count) of 200000, cost 2 (hash-func [21:SHA1 22:SHA256]) of 22
Raw:    392 c/s real, 98.8 c/s virtual

Benchmarking: ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Speed for cost 1 (HMAC size) of 0
Raw:    89663 c/s real, 22784 c/s virtual

Benchmarking: ZipMonster, MD5(ZipMonster) [MD5-256/256 AVX2 8x3 x 50000]... (4xOMP) DONE
Raw:    4473 c/s real, 1162 c/s virtual

Benchmarking: plaintext, $0$ [n/a]... DONE
Raw:    123930K c/s real, 124553K c/s virtual

Benchmarking: has-160 [HAS-160 32/64]... DONE
Raw:    8760K c/s real, 8804K c/s virtual

Benchmarking: HMAC-MD5 [password is key, MD5 256/256 AVX2 8x3]... (4xOMP) DONE
Many salts:     125079K c/s real, 33759K c/s virtual
Only one salt:  26726K c/s real, 6861K c/s virtual

Benchmarking: HMAC-SHA1 [password is key, SHA1 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     66256K c/s real, 17505K c/s virtual
Only one salt:  15138K c/s real, 3937K c/s virtual

Benchmarking: HMAC-SHA224 [password is key, SHA224 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     35045K c/s real, 8974K c/s virtual
Only one salt:  12247K c/s real, 3181K c/s virtual

Benchmarking: HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x]... (4xOMP) DONE
Many salts:     34148K c/s real, 8812K c/s virtual
Only one salt:  13180K c/s real, 3341K c/s virtual

Benchmarking: HMAC-SHA384 [password is key, SHA384 256/256 AVX2 4x]... (4xOMP) DONE
Many salts:     12724K c/s real, 3275K c/s virtual
Only one salt:  4984K c/s real, 1338K c/s virtual

Benchmarking: HMAC-SHA512 [password is key, SHA512 256/256 AVX2 4x]... (4xOMP) DONE
Many salts:     13512K c/s real, 3420K c/s virtual
Only one salt:  5949K c/s real, 1515K c/s virtual

Benchmarking: dynamic_0 [md5($p) (raw-md5) 256/256 AVX2 8x3]... DONE
Raw:    52704K c/s real, 52704K c/s virtual

Benchmarking: dynamic_1 [md5($p.$s) (joomla) 256/256 AVX2 8x3]... DONE
Many salts:     27148K c/s real, 27148K c/s virtual
Only one salt:  20013K c/s real, 20013K c/s virtual

Benchmarking: dynamic_2 [md5(md5($p)) (e107) 256/256 AVX2 8x3]... DONE
Raw:    26495K c/s real, 26495K c/s virtual

Benchmarking: dynamic_3 [md5(md5(md5($p))) 256/256 AVX2 8x3]... DONE
Raw:    18905K c/s real, 19000K c/s virtual

Benchmarking: dynamic_4 [md5($s.$p) (OSC) 256/256 AVX2 8x3]... DONE
Many salts:     34073K c/s real, 34073K c/s virtual
Only one salt:  20391K c/s real, 20391K c/s virtual

Benchmarking: dynamic_5 [md5($s.$p.$s) 256/256 AVX2 8x3]... DONE
Many salts:     24155K c/s real, 24155K c/s virtual
Only one salt:  16458K c/s real, 16458K c/s virtual

Benchmarking: dynamic_6 [md5(md5($p).$s) 256/256 AVX2 8x3]... DONE
Many salts:     50161K c/s real, 50161K c/s virtual
Only one salt:  15081K c/s real, 15081K c/s virtual

Benchmarking: dynamic_8 [md5(md5($s).$p) 256/256 AVX2 8x3]... DONE
Many salts:     36414K c/s real, 36596K c/s virtual
Only one salt:  23864K c/s real, 23864K c/s virtual

Benchmarking: dynamic_9 [md5($s.md5($p)) 256/256 AVX2 8x3]... DONE
Many salts:     34114K c/s real, 34114K c/s virtual
Only one salt:  15165K c/s real, 15165K c/s virtual

Benchmarking: dynamic_10 [md5($s.md5($s.$p)) 256/256 AVX2 8x3]... DONE
Many salts:     16416K c/s real, 16416K c/s virtual
Only one salt:  13164K c/s real, 13164K c/s virtual

Benchmarking: dynamic_11 [md5($s.md5($p.$s)) 256/256 AVX2 8x3]... DONE
Many salts:     16610K c/s real, 16610K c/s virtual
Only one salt:  13290K c/s real, 13290K c/s virtual

Benchmarking: dynamic_12 [md5(md5($s).md5($p)) (IPB) 256/256 AVX2 8x3]... DONE
Many salts:     21210K c/s real, 21210K c/s virtual
Only one salt:  9478K c/s real, 9478K c/s virtual

Benchmarking: dynamic_13 [md5(md5($p).md5($s)) 256/256 AVX2 8x3]... DONE
Many salts:     21210K c/s real, 21316K c/s virtual
Only one salt:  9443K c/s real, 9443K c/s virtual

Benchmarking: dynamic_14 [md5($s.md5($p).$s) 256/256 AVX2 8x3]... DONE
Many salts:     24161K c/s real, 24283K c/s virtual
Only one salt:  12786K c/s real, 12786K c/s virtual

Benchmarking: dynamic_15 [md5($u.md5($p).$s) 256/256 AVX2 8x3]... DONE
Many salts:     16484K c/s real, 16484K c/s virtual
Only one salt:  8176K c/s real, 8176K c/s virtual

Benchmarking: dynamic_16 [md5(md5(md5($p).$s).$s2) 256/256 AVX2 8x3]... DONE
Many salts:     11546K c/s real, 11546K c/s virtual
Only one salt:  6872K c/s real, 6872K c/s virtual

Benchmarking: dynamic_18 [md5($s.Y.$p.0xF7.$s) (Post.Office MD5) 32/64 x2]... DONE
Many salts:     5256K c/s real, 5256K c/s virtual
Only one salt:  4917K c/s real, 4917K c/s virtual

Benchmarking: dynamic_19 [md5($p) (Cisco PIX) 256/256 AVX2 8x3]... DONE
Raw:    26122K c/s real, 26122K c/s virtual

Benchmarking: dynamic_20 [md5($p.$s) (Cisco ASA) 256/256 AVX2 8x3]... DONE
Many salts:     30392K c/s real, 30241K c/s virtual
Only one salt:  19960K c/s real, 19960K c/s virtual

Benchmarking: dynamic_22 [md5(sha1($p)) 256/256 AVX2 8x1]... DONE
Raw:    11575K c/s real, 11575K c/s virtual

Benchmarking: dynamic_23 [sha1(md5($p)) 256/256 AVX2 8x1]... DONE
Raw:    15792K c/s real, 15792K c/s virtual

Benchmarking: dynamic_24 [sha1($p.$s) 256/256 AVX2 8x1]... DONE
Many salts:     16974K c/s real, 17060K c/s virtual
Only one salt:  14318K c/s real, 14247K c/s virtual

Benchmarking: dynamic_25 [sha1($s.$p) 256/256 AVX2 8x1]... DONE
Many salts:     18123K c/s real, 18214K c/s virtual
Only one salt:  13967K c/s real, 13967K c/s virtual

Benchmarking: dynamic_26 [sha1($p) raw-sha1 256/256 AVX2 8x1]... DONE
Raw:    19760K c/s real, 19760K c/s virtual

Benchmarking: dynamic_29 [md5(utf16($p)) 256/256 AVX2 8x3]... DONE
Raw:    23197K c/s real, 23197K c/s virtual

Benchmarking: dynamic_30 [md4($p) (raw-md4) 256/256 AVX2 8x3]... DONE
Raw:    65632K c/s real, 65962K c/s virtual

Benchmarking: dynamic_31 [md4($s.$p) 256/256 AVX2 8x3]... DONE
Many salts:     40840K c/s real, 40840K c/s virtual
Only one salt:  25238K c/s real, 25365K c/s virtual

Benchmarking: dynamic_32 [md4($p.$s) 256/256 AVX2 8x3]... DONE
Many salts:     34238K c/s real, 34410K c/s virtual
Only one salt:  22579K c/s real, 22466K c/s virtual

Benchmarking: dynamic_33 [md4(utf16($p)) 256/256 AVX2 8x3]... DONE
Raw:    29225K c/s real, 29225K c/s virtual

Benchmarking: dynamic_34 [md5(md4($p)) 256/256 AVX2 8x3]... DONE
Raw:    30912K c/s real, 30912K c/s virtual

Benchmarking: dynamic_35 [sha1(uc($u).:.$p) (ManGOS) 256/256 AVX2 8x1]... DONE
Many salts:     14894K c/s real, 14894K c/s virtual
Only one salt:  12183K c/s real, 12183K c/s virtual

Benchmarking: dynamic_36 [sha1($u.:.$p) (ManGOS2) 256/256 AVX2 8x1]... DONE
Many salts:     14604K c/s real, 14677K c/s virtual
Only one salt:  11907K c/s real, 11848K c/s virtual

Benchmarking: dynamic_37 [sha1(lc($u).$p) (SMF) 256/256 AVX2 8x1]... DONE
Many salts:     17352K c/s real, 17352K c/s virtual
Only one salt:  13957K c/s real, 13957K c/s virtual

Benchmarking: dynamic_38 [sha1($s.sha1($s.sha1($p))) (Wolt3BB) 256/256 AVX2 8x1]... DONE
Many salts:     4752K c/s real, 4752K c/s virtual
Only one salt:  4092K c/s real, 4092K c/s virtual

Benchmarking: dynamic_39 [md5($s.pad16($p)) (net-md5) 256/256 AVX2 8x3]... DONE
Many salts:     11744K c/s real, 11744K c/s virtual
Only one salt:  8924K c/s real, 8924K c/s virtual

Benchmarking: dynamic_40 [sha1($s.pad20($p)) (net-sha1) 256/256 AVX2 8x1]... DONE
Many salts:     11319K c/s real, 11319K c/s virtual
Only one salt:  10998K c/s real, 10998K c/s virtual

Benchmarking: dynamic_50 [sha224($p) 256/256 AVX2 8x]... DONE
Raw:    12836K c/s real, 12836K c/s virtual

Benchmarking: dynamic_60 [sha256($p) 256/256 AVX2 8x]... DONE
Raw:    12569K c/s real, 12507K c/s virtual

Benchmarking: dynamic_61 [sha256($s.$p) 256/256 AVX2 8x]... DONE
Many salts:     10116K c/s real, 10116K c/s virtual
Only one salt:  8909K c/s real, 8909K c/s virtual

Benchmarking: dynamic_62 [sha256($p.$s) 256/256 AVX2 8x]... DONE
Many salts:     10414K c/s real, 10414K c/s virtual
Only one salt:  8789K c/s real, 8789K c/s virtual

Benchmarking: dynamic_70 [sha384($p) 256/256 AVX2 4x]... DONE
Raw:    6693K c/s real, 6693K c/s virtual

Benchmarking: dynamic_80 [sha512($p) 256/256 AVX2 4x]... DONE
Raw:    6380K c/s real, 6380K c/s virtual

Benchmarking: dynamic_82 [sha512($p.$s) 256/256 AVX2 4x]... DONE
Many salts:     5834K c/s real, 5834K c/s virtual
Only one salt:  5468K c/s real, 5468K c/s virtual

Benchmarking: dynamic_90 [gost($p) 64/64]... DONE
Raw:    700560 c/s real, 700560 c/s virtual

Benchmarking: dynamic_100 [whirlpool($p) 32/64 OpenSSL]... DONE
Raw:    2320K c/s real, 2320K c/s virtual

Benchmarking: dynamic_110 [tiger($p) 32/64 sph_tiger]... DONE
Raw:    6821K c/s real, 6856K c/s virtual

Benchmarking: dynamic_120 [ripemd128($p) 32/64 sph_ripemd]... DONE
Raw:    6788K c/s real, 6755K c/s virtual

Benchmarking: dynamic_130 [ripemd160($p) 32/64 sph_ripemd]... DONE
Raw:    4462K c/s real, 4462K c/s virtual

Benchmarking: dynamic_140 [ripemd256($p) 32/64 sph_ripemd]... DONE
Raw:    5980K c/s real, 5980K c/s virtual

Benchmarking: dynamic_150 [ripemd320($p) 32/64 sph_ripemd]... DONE
Raw:    4194K c/s real, 4194K c/s virtual

Benchmarking: dynamic_160 [haval128_3($p) 32/64 sph_haval]... DONE
Raw:    4756K c/s real, 4756K c/s virtual

Benchmarking: dynamic_170 [haval128_4($p) 32/64 sph_haval]... DONE
Raw:    3403K c/s real, 3403K c/s virtual

Benchmarking: dynamic_180 [haval128_5($p) 32/64 sph_haval]... DONE
Raw:    2983K c/s real, 2983K c/s virtual

Benchmarking: dynamic_190 [haval160_3($p) 32/64 sph_haval]... DONE
Raw:    4749K c/s real, 4725K c/s virtual

Benchmarking: dynamic_200 [haval160_4($p) 32/64 sph_haval]... DONE
Raw:    3405K c/s real, 3405K c/s virtual

Benchmarking: dynamic_210 [haval160_5($p) 32/64 sph_haval]... DONE
Raw:    2940K c/s real, 2940K c/s virtual

Benchmarking: dynamic_220 [haval192_3($p) 32/64 sph_haval]... DONE
Raw:    4446K c/s real, 4424K c/s virtual

Benchmarking: dynamic_230 [haval192_4($p) 32/64 sph_haval]... DONE
Raw:    3003K c/s real, 2988K c/s virtual

Benchmarking: dynamic_240 [haval192_5($p) 32/64 sph_haval]... DONE
Raw:    2917K c/s real, 2931K c/s virtual

Benchmarking: dynamic_250 [haval224_3($p) 32/64 sph_haval]... DONE
Raw:    4806K c/s real, 4806K c/s virtual

Benchmarking: dynamic_260 [haval224_4($p) 32/64 sph_haval]... DONE
Raw:    3292K c/s real, 3309K c/s virtual

Benchmarking: dynamic_270 [haval224_5($p) 32/64 sph_haval]... DONE
Raw:    3018K c/s real, 3018K c/s virtual

Benchmarking: dynamic_280 [haval256_3($p) 32/64 sph_haval]... DONE
Raw:    4861K c/s real, 4885K c/s virtual

Benchmarking: dynamic_290 [haval256_4($p) 32/64 sph_haval]... DONE
Raw:    3435K c/s real, 3435K c/s virtual

Benchmarking: dynamic_300 [haval256_5($p) 32/64 sph_haval]... DONE
Raw:    2968K c/s real, 2968K c/s virtual

Benchmarking: dynamic_310 [md2($p) 32/64 sph_md2]... DONE
Raw:    292537 c/s real, 292537 c/s virtual

Benchmarking: dynamic_320 [panama($p) 32/64 sph_panama]... DONE
Raw:    1187K c/s real, 1187K c/s virtual

Benchmarking: dynamic_330 [skein224($p) 32/64 sph_skein]... DONE
Raw:    3879K c/s real, 3879K c/s virtual

Benchmarking: dynamic_340 [skein256($p) 32/64 sph_skein]... DONE
Raw:    3912K c/s real, 3912K c/s virtual

Benchmarking: dynamic_350 [skein384($p) 32/64 sph_skein]... DONE
Raw:    3860K c/s real, 3841K c/s virtual

Benchmarking: dynamic_360 [skein512($p) 32/64 sph_skein]... DONE
Raw:    3944K c/s real, 3944K c/s virtual

Benchmarking: dynamic_370 [sha3_224($p) 64/64 keccak]... DONE
Raw:    1864K c/s real, 1864K c/s virtual

Benchmarking: dynamic_380 [sha3_256($p) 64/64 keccak]... DONE
Raw:    1838K c/s real, 1848K c/s virtual

Benchmarking: dynamic_390 [sha3_384($p) 64/64 keccak]... DONE
Raw:    1928K c/s real, 1928K c/s virtual

Benchmarking: dynamic_400 [sha3_512($p) 64/64 keccak]... DONE
Raw:    1873K c/s real, 1873K c/s virtual

Benchmarking: dynamic_410 [keccak_256($p) 64/64 keccak]... DONE
Raw:    1908K c/s real, 1918K c/s virtual

Benchmarking: dynamic_420 [keccak_512($p) 64/64 keccak]... DONE
Raw:    1839K c/s real, 1848K c/s virtual

Benchmarking: dynamic_430 [keccak_224($p) 64/64 keccak]... DONE
Raw:    1938K c/s real, 1938K c/s virtual

Benchmarking: dynamic_440 [keccak_384($p) 64/64 keccak]... DONE
Raw:    1955K c/s real, 1955K c/s virtual

Benchmarking: dynamic_1001 [md5(md5(md5(md5($p)))) 256/256 AVX2 8x3]... DONE
Raw:    13043K c/s real, 13109K c/s virtual

Benchmarking: dynamic_1002 [md5(md5(md5(md5(md5($p))))) 256/256 AVX2 8x3]... DONE
Raw:    10488K c/s real, 10488K c/s virtual

Benchmarking: dynamic_1003 [md5(md5($p).md5($p)) 256/256 AVX2 8x3]... DONE
Raw:    10143K c/s real, 10143K c/s virtual

Benchmarking: dynamic_1004 [md5(md5(md5(md5(md5(md5($p)))))) 256/256 AVX2 8x3]... DONE
Raw:    9070K c/s real, 9070K c/s virtual

Benchmarking: dynamic_1005 [md5(md5(md5(md5(md5(md5(md5($p))))))) 256/256 AVX2 8x3]... DONE
Raw:    7837K c/s real, 7837K c/s virtual

Benchmarking: dynamic_1006 [md5(md5(md5(md5(md5(md5(md5(md5($p)))))))) 256/256 AVX2 8x3]... DONE
Raw:    6891K c/s real, 6891K c/s virtual

Benchmarking: dynamic_1007 [md5(md5($p).$s) (vBulletin) 256/256 AVX2 8x3]... DONE
Many salts:     50724K c/s real, 50724K c/s virtual
Only one salt:  15029K c/s real, 15029K c/s virtual

Benchmarking: dynamic_1008 [md5($p.$s) (RADIUS User-Password) 256/256 AVX2 8x3]... DONE
Many salts:     29887K c/s real, 29887K c/s virtual
Only one salt:  20044K c/s real, 20044K c/s virtual

Benchmarking: dynamic_1009 [md5($s.$p) (RADIUS Responses) 256/256 AVX2 8x3]... DONE
Many salts:     34455K c/s real, 34455K c/s virtual
Only one salt:  23454K c/s real, 23454K c/s virtual

Benchmarking: dynamic_1010 [md5($p null_padded_to_len_100) RAdmin v2.x MD5 256/256 AVX2 8x3]... DONE
Raw:    17376K c/s real, 17463K c/s virtual

Benchmarking: dynamic_1011 [md5($p.md5($s)) (webEdition CMS) 256/256 AVX2 8x3]... DONE
Many salts:     12954K c/s real, 12954K c/s virtual
Only one salt:  10170K c/s real, 10170K c/s virtual

Benchmarking: dynamic_1012 [md5($p.md5($s)) (webEdition CMS) 256/256 AVX2 8x3]... DONE
Many salts:     25952K c/s real, 25952K c/s virtual
Only one salt:  18454K c/s real, 18454K c/s virtual

Benchmarking: dynamic_1013 [md5($p.PMD5(username)) (webEdition CMS) 256/256 AVX2 8x3]... DONE
Many salts:     27538K c/s real, 27538K c/s virtual
Only one salt:  18950K c/s real, 18950K c/s virtual

Benchmarking: dynamic_1014 [md5($p.$s) (long salt) 256/256 AVX2 8x3]... DONE
Many salts:     12788K c/s real, 12788K c/s virtual
Only one salt:  9817K c/s real, 9817K c/s virtual

Benchmarking: dynamic_1015 [md5(md5($p.$u).$s) (PostgreSQL 'pass the hash') 256/256 AVX2 8x3]... DONE
Many salts:     16049K c/s real, 16049K c/s virtual
Only one salt:  12751K c/s real, 12751K c/s virtual

Benchmarking: dynamic_1016 [md5($p.$s) (long salt) 256/256 AVX2 8x3]... DONE
Many salts:     16455K c/s real, 16455K c/s virtual
Only one salt:  12677K c/s real, 12677K c/s virtual

Benchmarking: dynamic_1017 [md5($s.$p) (long salt) 256/256 AVX2 8x3]... DONE
Many salts:     12925K c/s real, 12925K c/s virtual
Only one salt:  11257K c/s real, 11257K c/s virtual

Benchmarking: dynamic_1018 [md5(sha1(sha1($p))) 256/256 AVX2 8x1]... DONE
Raw:    7956K c/s real, 7956K c/s virtual

Benchmarking: dynamic_1019 [md5(sha1(sha1(md5($p)))) 256/256 AVX2 8x1]... DONE
Raw:    6683K c/s real, 6683K c/s virtual

Benchmarking: dynamic_1020 [md5(sha1(md5($p))) 256/256 AVX2 8x1]... DONE
Raw:    10195K c/s real, 10195K c/s virtual

Benchmarking: dynamic_1021 [md5(sha1(md5(sha1($p)))) 256/256 AVX2 8x1]... DONE
Raw:    5745K c/s real, 5745K c/s virtual

Benchmarking: dynamic_1022 [md5(sha1(md5(sha1(md5($p))))) 256/256 AVX2 8x1]... DONE
Raw:    5431K c/s real, 5431K c/s virtual

Benchmarking: dynamic_1023 [sha1($p) (hash truncated to length 32) 256/256 AVX2 8x1]... DONE
Raw:    17861K c/s real, 17861K c/s virtual

Benchmarking: dynamic_1024 [sha1(md5($p)) (hash truncated to length 32) 256/256 AVX2 8x1]... DONE
Raw:    14340K c/s real, 14340K c/s virtual

Benchmarking: dynamic_1025 [sha1(md5(md5($p))) (hash truncated to length 32) 256/256 AVX2 8x1]... DONE
Raw:    9750K c/s real, 9799K c/s virtual

Benchmarking: dynamic_1026 [sha1(sha1($p)) (hash truncated to length 32) 256/256 AVX2 8x1]... DONE
Raw:    9947K c/s real, 9947K c/s virtual

Benchmarking: dynamic_1027 [sha1(sha1(sha1($p))) (hash truncated to length 32) 256/256 AVX2 8x1]... DONE
Raw:    7178K c/s real, 7178K c/s virtual

Benchmarking: dynamic_1028 [sha1(sha1_raw($p)) (hash truncated to length 32) 256/256 AVX2 8x1]... DONE
Raw:    10686K c/s real, 10686K c/s virtual

Benchmarking: dynamic_1029 [sha256($p) (hash truncated to length 32) 256/256 AVX2 8x]... DONE
Raw:    8430K c/s real, 8430K c/s virtual

Benchmarking: dynamic_1030 [whirlpool($p) (hash truncated to length 32) 32/64 OpenSSL]... DONE
Raw:    2049K c/s real, 2049K c/s virtual

Benchmarking: dynamic_1031 [gost($p) (hash truncated to length 32) 64/64]... DONE
Raw:    633552 c/s real, 633552 c/s virtual

Benchmarking: dynamic_1032 [sha1_64(utf16($p)) (PeopleSoft) 256/256 AVX2 8x1]... DONE
Raw:    12722K c/s real, 12722K c/s virtual

Benchmarking: dynamic_1034 [md5($p.$u) (PostgreSQL MD5) 256/256 AVX2 8x3]... DONE
Many salts:     28817K c/s real, 28817K c/s virtual
Only one salt:  18506K c/s real, 18506K c/s virtual

Benchmarking: dynamic_1300 [md5(md5_raw($p)) 256/256 AVX2 8x3]... DONE
Raw:    19177K c/s real, 19177K c/s virtual

Benchmarking: dynamic_1350 [md5(md5($s.$p):$s) 256/256 AVX2 8x3]... DONE
Many salts:     13928K c/s real, 13928K c/s virtual
Only one salt:  10970K c/s real, 11309K c/s virtual

Benchmarking: dynamic_1400 [sha1(utf16($p)) (Microsoft CREDHIST) 256/256 AVX2 8x1]... DONE
Raw:    9337K c/s real, 9431K c/s virtual

Benchmarking: dynamic_1401 [md5($u.\nskyper\n.$p) (Skype MD5) 256/256 AVX2 8x3]... DONE
Many salts:     7432K c/s real, 7432K c/s virtual
Only one salt:  6778K c/s real, 6812K c/s virtual

Benchmarking: dynamic_1501 [sha1($s.sha1($p)) (Redmine) 256/256 AVX2 8x1]... DONE
Many salts:     13043K c/s real, 13043K c/s virtual
Only one salt:  6654K c/s real, 6621K c/s virtual

Benchmarking: dynamic_1502 [sha1(sha1($p).$s) (XenForo SHA-1) 256/256 AVX2 8x1]... DONE
Many salts:     23084K c/s real, 23084K c/s virtual
Only one salt:  8599K c/s real, 8643K c/s virtual

Benchmarking: dynamic_1503 [sha256(sha256($p).$s) (XenForo SHA-256) 256/256 AVX2 8x]... DONE
Many salts:     5386K c/s real, 5359K c/s virtual
Only one salt:  3255K c/s real, 3255K c/s virtual

Benchmarking: dynamic_1504 [sha1($s.$p.$s) 256/256 AVX2 8x1]... DONE
Many salts:     14567K c/s real, 14567K c/s virtual
Only one salt:  12205K c/s real, 12205K c/s virtual

Benchmarking: dynamic_1505 [md5($p.$s.md5($p.$s)) 256/256 AVX2 8x3]... DONE
Many salts:     6258K c/s real, 6289K c/s virtual
Only one salt:  5651K c/s real, 5651K c/s virtual

Benchmarking: dynamic_1506 [md5($u.:XDB:.$p) (Oracle 12c "H" hash) 256/256 AVX2 8x3]... DONE
Many salts:     26305K c/s real, 26305K c/s virtual
Only one salt:  18229K c/s real, 18229K c/s virtual

Benchmarking: dynamic_1507 [sha1(utf16($const.$p)) (Mcafee master pass) 256/256 AVX2 8x1]... DONE
Raw:    11282K c/s real, 11282K c/s virtual

Benchmarking: dynamic_1518 [md5(sha1($p).md5($p).sha1($p)) 256/256 AVX2 8x1]... DONE
Raw:    5318K c/s real, 5318K c/s virtual

Benchmarking: dynamic_1528 [sha256($s.$p.$s) (Telegram for Android) 256/256 AVX2 8x]... DONE
Many salts:     9858K c/s real, 9809K c/s virtual
Only one salt:  8562K c/s real, 8605K c/s virtual

Benchmarking: dynamic_1529 [sha1($p null_padded_to_len_32) (DeepSound) 256/256 AVX2 8x1]... DONE
Raw:    13346K c/s real, 13413K c/s virtual

Benchmarking: dynamic_1550 [md5($u.:mongo:.$p) (MONGODB-CR system hash) 256/256 AVX2 8x3]... DONE
Many salts:     22762K c/s real, 22762K c/s virtual
Only one salt:  16915K c/s real, 16915K c/s virtual

Benchmarking: dynamic_1551 [md5($s.$u.(md5($u.:mongo:.$p)) (MONGODB-CR network hash) 256/256 AVX2 8x3]... DONE
Many salts:     11649K c/s real, 11649K c/s virtual
Only one salt:  9508K c/s real, 9461K c/s virtual

Benchmarking: dynamic_1552 [md5($s.$u.(md5($u.:mongo:.$p)) (MONGODB-CR network hash) 256/256 AVX2 8x3]... DONE
Many salts:     7025K c/s real, 7025K c/s virtual
Only one salt:  6363K c/s real, 6395K c/s virtual

Benchmarking: dynamic_1560 [md5($s.$p.$s2) (SocialEngine) 256/256 AVX2 8x3]... DONE
Many salts:     13723K c/s real, 13723K c/s virtual
Only one salt:  11094K c/s real, 11150K c/s virtual

Benchmarking: dynamic_1588 [sha256($s.sha1($p)) (ColdFusion 11) 256/256 AVX2 8x]... DONE
Many salts:     4919K c/s real, 4943K c/s virtual
Only one salt:  4633K c/s real, 4633K c/s virtual

Benchmarking: dynamic_1590 [sha1(utf16be(space_pad_10(uc($s)).$p)) (IBM AS/400 SHA1) 256/256 AVX2 8x1]... DONE
Many salts:     14577K c/s real, 14577K c/s virtual
Only one salt:  11544K c/s real, 11544K c/s virtual

Benchmarking: dynamic_1592 [sha1($s.sha1($s.sha1($p))) (wbb3) 256/256 AVX2 8x1]... DONE
Many salts:     6498K c/s real, 6498K c/s virtual
Only one salt:  4376K c/s real, 4376K c/s virtual

Benchmarking: dynamic_1600 [sha1($s.utf16le($p)) (Oracle PeopleSoft PS_TOKEN) 256/256 AVX2 8x1]... DONE
Many salts:     9340K c/s real, 9340K c/s virtual
Only one salt:  7590K c/s real, 7590K c/s virtual

Benchmarking: dynamic_1602 [sha256(#.$salt.-.$pass) (QAS vas_auth) 256/256 AVX2 8x]... DONE
Many salts:     8302K c/s real, 8302K c/s virtual
Only one salt:  7257K c/s real, 7257K c/s virtual

Benchmarking: dynamic_1608 [sha256(sha256_raw(sha256_raw($p))) (Neo Wallet) 256/256 AVX2 8x]... DONE
Raw:    4379K c/s real, 4379K c/s virtual

Benchmarking: dynamic_2000 [md5($p) (PW > 55 bytes) 256/256 AVX2 8x3]... DONE
Raw:    22453K c/s real, 22453K c/s virtual

Benchmarking: dynamic_2001 [md5($p.$s) (joomla) (PW > 23 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     20034K c/s real, 20034K c/s virtual
Only one salt:  15610K c/s real, 15610K c/s virtual

Benchmarking: dynamic_2002 [md5(md5($p)) (e107) (PW > 55 bytes) 256/256 AVX2 8x3]... DONE
Raw:    13166K c/s real, 13166K c/s virtual

Benchmarking: dynamic_2003 [md5(md5(md5($p))) (PW > 55 bytes) 256/256 AVX2 8x3]... DONE
Raw:    9799K c/s real, 9799K c/s virtual

Benchmarking: dynamic_2004 [md5($s.$p) (OSC) (PW > 31 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     20966K c/s real, 20966K c/s virtual
Only one salt:  16012K c/s real, 16012K c/s virtual

Benchmarking: dynamic_2005 [md5($s.$p.$s) (PW > 31 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     16222K c/s real, 16222K c/s virtual
Only one salt:  13623K c/s real, 13623K c/s virtual

Benchmarking: dynamic_2006 [md5(md5($p).$s) (vBulletin, PW > 55 bytes or/and salt > 23 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     27229K c/s real, 27229K c/s virtual
Only one salt:  10794K c/s real, 10794K c/s virtual

Benchmarking: dynamic_2008 [md5(md5($s).$p) (PW > 23 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     22224K c/s real, 22224K c/s virtual
Only one salt:  16596K c/s real, 16596K c/s virtual

Benchmarking: dynamic_2009 [md5($s.md5($p)) (salt > 23 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     22238K c/s real, 22238K c/s virtual
Only one salt:  9035K c/s real, 9035K c/s virtual

Benchmarking: dynamic_2010 [md5($s.md5($s.$p)) (PW > 32 or salt > 23 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     11025K c/s real, 11025K c/s virtual
Only one salt:  9280K c/s real, 9280K c/s virtual

Benchmarking: dynamic_2011 [md5($s.md5($p.$s)) (PW > 32 or salt > 23 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     11091K c/s real, 11091K c/s virtual
Only one salt:  9434K c/s real, 9434K c/s virtual

Benchmarking: dynamic_2014 [md5($s.md5($p).$s) (PW > 55 or salt > 11 bytes) 256/256 AVX2 8x3]... DONE
Many salts:     16539K c/s real, 16539K c/s virtual
Only one salt:  7959K c/s real, 7959K c/s virtual

Benchmarking: dummy [N/A]... DONE
Raw:    70332K c/s real, 70332K c/s virtual

Benchmarking: crypt, generic crypt(3) [?/64]... (4xOMP) DONE
Speed for cost 1 (algorithm [1:descrypt 2:md5crypt 3:sunmd5 4:bcrypt 5:sha256crypt 6:sha512crypt]) of 1, cost 2 (algorithm specific iterations) of 1
Many salts:     689856 c/s real, 181064 c/s virtual
Only one salt:  718128 c/s real, 185562 c/s virtual

416 formats benchmarked.
