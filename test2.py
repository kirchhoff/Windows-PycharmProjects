#coding=utf-8
s={}
references='''
1. Liu F, Shu P, Jin H, Ding L, Yu J, Niu D, Li B (2013) Gearing resource-poor mobile devices with powerful clouds: architectures, challenges, and applications. IEEE Wirel Comm 20:2–10
2. Chen M, JinH, Wen Y, Leung VCM(2013) Enabling technologies for future data center networking: a primer. IEEE Netw 27(4):8–15
3. Fernando N, Loke SW, Rahayu W (2013) Mobile cloud computing: a survey. Fut Gen Comp Sys 29(1):84–106
4. Chen M, Ma Y, Ullah S, Cai W, Song E (2013) ROCHAS:robotics and cloud-assisted healthcare system for empty nester. In:BodyNets’13
5. Kumar K, Liu J, Lu Y-H, Bhargava B (2013) A survey of computation offloading for mobile systems. ACM/Springer MONET 18:129–140
6. Sanaei Z, Abolfazli S, Gani A, Buyya R (2013) Heterogeneity in mobile cloud computing: taxonomy and open challenges. IEEE Comm Surv Tut 99:1–24
7. Li Q, Clark G (2013) Mobile security: a look ahead. IEEE Secur Priv 11(1):78–81
8. Khan AN, Kiah MLM, Khan SU, Madani SA (2013) Towards secure mobile cloud computing: a survey. Fut Gen Comp Sys 29(5):1278–1299
9. Heavy Reading Real World Research (2013) The mobile cloud market outlook to 2017
10. Fernando N, Loke SW, Rahayu W (2013) Mobile cloud computing: a survey. In: Future generation of computing systems
11. Braunstein ML (2013) Health informatics in the cloud. Springer
12. Rahimi MR, Venkatasubramanian N, Vasilakos A (2013) MuSIC: on mobility-aware optimal service allocation in mobile cloud computing. In: The IEEE cloud’13
13. Liang H, Cai LX, Huang D, Shen XS, Peng D (2012) An SMDP-based service model for inter-domain resource allocation in mobile cloud networks. In: IEEE transactions on vehicular technology
14. Papazoglou MP (2012) Cloud blueprints for integrating and managing cloud federations. In: Springer software service and application engineering
15. Kosta S, Aucinas A, Hui P, Mortier R, Zhang X (2012) ThinkAir: dynamic resource allocation and parallel execution in the cloud for mobile code offloading. In: IEEE INFOCOM’12, pp 945–95
16. Rahimi MR, Venkatasubramanian N, Mehrotra S, Vasilakos AV(2012) MAPCloud: mobile applications on an elastic and scalable 2-tier cloud architecture. In: IEEE/ACM UCC’12, pp 83–90
17. Kemp R, Palmer N, Kielmann T, Bal H (2012) Cuckoo: a computation offloading framework for smartphones. In: Mobile computing application and service, vol 76 of LNCS. Springer, pp 59–79
18. Kim K-H, Lee S-J, Congdon P (2012) On cloud-centric network architecture for multi-dimensional mobility. SIGCOMM Comput Commun Rev 42:509–514
19. Wen Y, Zhang W, Luo H (2012) Energy optimal mobile application eexecution: taming resource-poor mobile devices with cloud Clones. In: IEEE international conference on computer communications, INFOCOM
20. Pitkänen M, Kärkkäinen T, Ott J, Conti M, Passarella A, Giordano S, Puccinelli D, Legendre F, Trifunovic S, Hummel K, May M, Hegde N, Spyropoulos T (2012) SCAMPI: service platform for social aware mobile and pervasive computing. In: ACM proceedings of the first edition of the MCC workshop on mobile cloud computing, MCC ’12
21. Lovett T, ONeill E (2012) Mobile context awareness. Springer
22. Saylor M (2012) The mobile wave: how mobile intelligence will change everything. Perseus Books/Vanguard Press
23. Rahimi MR (2012) Exploiting an elastic 2-tiered cloud architecture for rich mobile applications. In: IEEE/ACM 13th international symposium on a world of wireless, mobile and multimedia networks
24. Chen M, Gonzalez S, Vasilakos A, Cao H, Leung VC (2011) Body area networks: a survey. ACM/Springer MONET 16:171–193
25. Chun B-G, Ihm S, Maniatis P, Naik M, Patti A (2011) CloneCloud: elastic execution between mobile device and cloud. In: ACM EuroSys ’11, pp 301–314
26. Subashini S, Kavitha V (2011) A survey on security issues in service delivery models of cloud computing. J Netw Comput App 34(1):1–11
27. Bilogrevic I, Jadliwala M, Kumar P, Walia SS, Hubaux J-P, Aad I, Niemi V (2011) Meetings through the cloud: privacy-preserving scheduling on mobile devices. J Syst Softw 84(11):1910–1927
28. Ngoc MD, Cheng-Hsin H, Singh JP, Venkatasubramanian N (2011) Massive live video distribution using hybrid cellular and Ad Hoc networks. In: IEEE WoWMoM
29. Berking P, Archibald T, Haag J, Birtwhistle M (2012) Mobile learning: not just another delivery method. In: The inter service/industry training, simulation and education conference(I/ITSEC)
30. Papakos P, Capra L, Rosenblum DS (2010) VOLARE: context-aware adaptive cloud service discovery for mobile systems. In:Proceedings of the 9th international workshop on adaptive and reflective middleware (ARM)
31. Mohapatra S, Rahimi MR, Venkatasubranian N (2011) Power-aware middleware for mobile applications. In: Chapter 10 of the handbook of energy-aware and green computing, ISBN: 978-1-4398-5040-4, Chapman and Hall/CRC
32. Dinh HT, Lee C, Niyato D, Wang P (2011) A survey of mobile cloud computing: architecture, applications, and approaches. In: Wireless communications and mobile computing
33. Ferzli R, Khalife I (2011) Mobile cloud computing educational tool for image/video processing algorithms. In: Digital signal processing workshop and IEEE signal processing education workshop (DSP/SPE)
34. Estrin D, Sim I (2010) Open mHealth architecture: an engine for health care innovation. Sci Mag, AAAS 330(6005):759–760
35. Satyanarayanan M (2011) Mobile computing: the next decade. SIGMOBILE Mob Comput Commun Rev 15:2–10
36. Gao H, Zhai Y (2010) System design of cloud computing based on mobile learning. In: Knowledge acquisition and modeling (KAM),pp 239–242
37. Yang X, Pan T, Shen J (2010) On 3G mobile E-commerce platform based on cloud computing. In: Ubi-media computing(U-Media), pp 198–201
38. Hoang DB, Chen L (2010) Mobile cloud for assistive healthcare(MoCAsH). In: IEEE APSCC’10, pp 325–332
39. Cuervo E, Balasubramanian A, Cho D, Wolman A, Saroiu S, Chandra R, Bahl P (2010) MAUI: making smartphones last longer with code offload. In: ACM MobiSys’10, pp 49–62
40. Huang D, Zhang X, Kang M, Luo J (2010) MobiCloud: building secure cloud framework for mobile computing and communication. In: IEEE SOSE’10, pp 27–34
41. Kristensen MD (2010) Scavenger: transparent development of efficient cyber foraging applications. In: IEEE PerCom’10, pp217–226
42. Kumar K, Lu Y-H (2010) Cloud computing for mobile users: can offloading computation save energy? IEEE Comput 43(4):51–56
43. Nimmagadda Y, Kumar K, Lu Y-H, Lee CSG (2010) Realtime moving object recognition and tracking using computation offloading. In: IEEE/RSJ intelligent robots and systems(IROS’10), pp 2449–2455
44. Itani W, Kayssi A, Chehab A (2010) Energy-efficient incremental integrity for securing storage in mobile cloud computing. In: IEEE ICEAC’10, pp 1–2
45. Liang H, Huang D, Cai LX, Shen X, Peng D (2011) Resource allocation for security services in mobile cloud computing. In: IEEE INFOCOM’11 workshops on M2MCN’11, pp 191–195
46. Yang X, Pan T, Shen J (2010) On 3G mobile e-commerce platform based on cloud computing. In: IEEE U-Media (2010)
47. Zhao W, Sun Y, Dai L (2010) Improving computer basis teaching through mobile communication and cloud computing technology. In: Proceedings of the 3rd international conference on advanced computer theory and engineering (ICACTE’10)
48. ABI (2009) Mobile cloud computing subscribers to total nearly one billion by 2014, Tech. Rep., ABI Research
49. Marinelli E (2009) Hyrax: cloud computing on mobile devices using MapReduce. Master thesis, Carnegie Mellon University
50. Satyanarayanan M, Bahl P, Caceres R, Davies N (2009) The case for VM-based cloudlets in mobile computing. IEEE Pervasive Comput 8(4):14–23
51. Khan AH, Qadeer MA, Ansari JA, Waheed S (2009) 4G as a next generation wireless network. In: IEEE international conference on future computer and communication, ICFCC
52. Giurgiu I, Riva O, Juric D, Krivulev I, Alonso G (2009) Calling the cloud: enabling mobile phones as interfaces to cloud applications. In: Proceedings of the ACM/IFIP/USENIX 10th international conference on Middleware, Middleware 2009
53. Dean J, Ghemawat S (2008) MapReduce: simplified data processing on large clusters. Commun ACM 51:107–113
54. Yang K, Ou S, Chen H-H (2008) On effective offloading services for resource-constrained mobile devices running heavier mobile Internet applications. IEEE Comm Mag 46:56–63
55. Huerta-Canepa G, Lee D (2008) An adaptable application offloading scheme based on application behavior. In: IEEE AINAW’08 workshop, pp 387–392
56. Yiu ML, Jensen CS, Huang X, Lu H (2008) SpaceTwist: managing the trade-offs among location privacy, query performance, and query accuracy in mobile services. In: IEEE ICDE’08, pp 366–375
57. Xian C, Lu Y-H, Li Z (2007) Adaptive computation offloading for energy conservation on battery-powered systems. In: Parallel and distance systems ’07, vol 2, pp 1–8
58. Mohapatra S, Dutt N, Nicolau A, Venkatasubramanian N (2007) DYNAMO: a cross-layer framework for end-to-end QoS and energy optimization in mobile handheld devices. In: IEEE journal on selected areas in communications
59. Katti S, Rahul H, Hu W, Katabi D, Médard M, Crowcroft J (2006) XORs in the air: practical wireless network coding. In: ACM SIGCOMM
60. Meingast M, Roosta T, SastryS(2006) Security and privacy issues with health care information technology. In: IEEE EMBS
61. Balan R, Satyanarayanan M, Park S, Okoshi T (2003) Tactics-based remote execution for mobile computing. In: MobiSys
62. Flinn J, Park S, Satyanarayanan M (2002) Balancing performance, energy, and quality in pervasive computing. In: IEEE international conference on distributed computing systems,ICDCS
63. Osborne MJ, Rubinstein A (1994) A course in game theory. MIT Press
'''
l=[]
for i in references.split('\n')[1:-1]:
    s[i.split('.')[0]]="".join(i.split(".")[1:])


l=['9', '3', '35', '2', '29', '22', '33', '47', '22', '37', '46', '11', '34', '60', '38', '24', '4', '10', '32', '10', '5', '5', '42', '50', '25', '17', '18', '52', '52', '61', '49', '39', '16', '40', '41', '62', '20', '15', '30', '39', '43', '54', '55', '57', '39', '25', '19', '19', '12', '16', '23', '51', '28', '59', '26', '7', '8', '27', '44', '45', '56', '13', '63', '14', '21']
w=set()
counter = 1
pp=[]
for i in l:
   if i not in w:
       w.add(i)
       if counter== 43:
           pp.append("[43]. Tang Z, Wang Z, Li P, et al. (2015) An application layer protocol for energy-efficient bandwidth aggregation with guaranteed quality-of-experience. IEEE Transactions on Parallel and Distributed Systems, 26(6): 1538-1546.")
           counter=counter+1
           pp.append("[%s].%s" % (counter, s[i]))
       else:
           pp.append("[%s].%s" % (counter, s[i]))
       counter=counter+1

for i in pp:
    print i

