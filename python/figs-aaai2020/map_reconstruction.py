import matplotlib.pyplot as plt

# geometry translation mtl
gt_mtl_lambda = [0, 0.2, 0.4, 0.6, 0.8]
gt_mtl_f1_bj = [0.3438, 0.3678, 0.3493, 0.3469, 0.336]
gt_mtl_f1_jn = [0.2108, 0.2156, 0.2145, 0.2093, 0.2065]
gt_mtl_precision_bj = [0.2741, 0.2879, 0.266, 0.2645, 0.2583]
gt_mtl_precision_jn = [0.1753, 0.1795, 0.1757, 0.1712, 0.17]
gt_mtl_recall_bj = [0.4778, 0.5245, 0.5239, 0.5179, 0.4983]
gt_mtl_recall_jn = [0.2964, 0.302, 0.3027, 0.2846, 0.2831]

# map reconstruction geo
mr_geo_x = [5, 10, 15, 20]

mr_geo_f1_bj_edelkamp = [0.194465319, 0.291012999, 0.353419662, 0.393516634]
mr_geo_f1_bj_cao = [0.356068141, 0.535440084, 0.627377943, 0.671156989]
mr_geo_f1_bj_biagioni = [0.192830857, 0.32867914, 0.432444385, 0.479022505]
mr_geo_f1_bj_chen = [0.287158311, 0.440594059, 0.534550932, 0.580249779]
mr_geo_f1_bj_kharita = [0.355723717, 0.51907596, 0.599902385, 0.623850718]
mr_geo_f1_bj_deep_mg_nt = [0.427712135, 0.621341237, 0.751659436, 0.782872663]
mr_geo_f1_bj_deep_mg = [0.435782055, 0.633947755, 0.75961749, 0.787101541]

mr_geo_f1_jn_edelkamp = [0.288877282, 0.420615883, 0.478017923, 0.501814333]
mr_geo_f1_jn_cao = [0.220311443, 0.327238815, 0.378863493, 0.411136775]
mr_geo_f1_jn_biagioni = [0.289360879, 0.469170329, 0.571635611, 0.636194297]
# mr_geo_f1_jn_chen = [0.396482589, 0.541730846, 0.585043145, 0.596300932]
mr_geo_f1_jn_chen = [0.32674077, 0.481213097, 0.546283234, 0.567839975]
mr_geo_f1_jn_kharita = [0.26807611, 0.486915222, 0.587358882, 0.652126736]
mr_geo_f1_jn_deep_mg_nt = [0.352423693, 0.565972437, 0.65733994, 0.693576981]
mr_geo_f1_jn_deep_mg = [0.36026283, 0.568563093, 0.65253012, 0.697655398]

mr_geo_precision_bj_edelkamp = [0.110946542, 0.174099428, 0.218103137, 0.24855086]
mr_geo_precision_bj_cao = [0.272245133, 0.448684955, 0.552328305, 0.608865428]
mr_geo_precision_bj_biagioni = [0.370541093, 0.61661777, 0.767263026, 0.803933877]
mr_geo_precision_bj_chen = [0.253091451, 0.427915321, 0.545018238, 0.608056826]
mr_geo_precision_bj_kharita = [0.29301099, 0.468595878, 0.557142048, 0.591870058]
mr_geo_precision_bj_deep_mg_nt = [0.508015656, 0.724327826, 0.856430624, 0.881929446]
mr_geo_precision_bj_deep_mg = [0.491128165, 0.716769805, 0.848430493, 0.876778366]

mr_geo_precision_jn_edelkamp = [0.206175959, 0.310000478, 0.355635736, 0.376730988]
mr_geo_precision_jn_cao = [0.139134979, 0.216278466, 0.25629823, 0.28385484]
mr_geo_precision_jn_biagioni = [0.394915105, 0.620792952, 0.731390728, 0.78611898]
mr_geo_precision_jn_chen = [0.384150498, 0.624079916, 0.724875267, 0.773169852]
mr_geo_precision_jn_kharita = [0.247890686, 0.460391593, 0.562352941, 0.626302626]
mr_geo_precision_jn_deep_mg_nt = [0.423893616, 0.669640246, 0.76746824, 0.800188798]
mr_geo_precision_jn_deep_mg = [0.418015718, 0.657898439, 0.75389755, 0.804464005]

mr_geo_recall_bj_edelkamp = [0.786620977, 0.885974263, 0.931091816, 0.944237258]
mr_geo_recall_bj_cao = [0.514471527, 0.663785883, 0.726029928, 0.747646954]
mr_geo_recall_bj_biagioni = [0.130326646, 0.22405391, 0.301065337, 0.341147221]
mr_geo_recall_bj_chen = [0.33182262, 0.454047057, 0.524478108, 0.5548748]
mr_geo_recall_bj_kharita = [0.452591163, 0.581745195, 0.649772021, 0.659484822]
mr_geo_recall_bj_deep_mg_nt = [0.369330917, 0.54399481, 0.669728408, 0.703820741]
mr_geo_recall_bj_deep_mg = [0.39164669, 0.568283189, 0.687636292, 0.714066839]

mr_geo_recall_jn_edelkamp = [0.482362632, 0.653966334, 0.728821733, 0.751244907]
mr_geo_recall_jn_cao = [0.528878767, 0.67200887, 0.726089053, 0.745359891]
mr_geo_recall_jn_biagioni = [0.228331638, 0.377073745, 0.469158879, 0.534296029]
mr_geo_recall_jn_chen = [0.409632716, 0.478580788, 0.490435621, 0.48528746]
mr_geo_recall_jn_kharita = [0.291840295, 0.516681786, 0.614692172, 0.680172024]
mr_geo_recall_jn_deep_mg_nt = [0.301576806, 0.49009954, 0.574851317, 0.612033694]
mr_geo_recall_jn_deep_mg = [0.316531027, 0.500588676, 0.575191164, 0.615884477]

# map reconstruction topo
mr_topo_x = [5, 10, 15, 20]
mr_topo_f1_bj_edelkamp = [0.201128146, 0.301274695, 0.369241364, 0.409847045]
mr_topo_f1_bj_cao = [0.351335052, 0.522537617, 0.600990959, 0.658747893]
mr_topo_f1_bj_biagioni = [0.139689316, 0.229176829, 0.291431552, 0.346866794]
mr_topo_f1_bj_chen = [0.279415547, 0.43185476, 0.514162437, 0.567051144]
mr_topo_f1_bj_kharita = [0.320034755, 0.461109091, 0.508570645, 0.530492179]
mr_topo_f1_bj_deep_mg_nt = [0.1524602658, 0.2262410155, 0.2828595453, 0.2923817404]
mr_topo_f1_bj_deep_mg = [0.4104015055, 0.6068618169, 0.7207729918, 0.7456638732]

mr_topo_f1_jn_edelkamp = [0.324580718, 0.46509282, 0.5100954, 0.546188883]
mr_topo_f1_jn_cao = [0.253912425, 0.374989649, 0.423848404, 0.451336523]
mr_topo_f1_jn_biagioni = [0.2594417787, 0.4294319994, 0.5425966373, 0.5917548459]
mr_topo_f1_jn_chen = [0.147591719, 0.204821225, 0.219149258, 0.248367053]
mr_topo_f1_jn_kharita = [0.24584011, 0.465749288, 0.555358843, 0.600460583]
mr_topo_f1_jn_deep_mg_nt = [0.117872468, 0.1693520115, 0.210950353, 0.2123343239]
mr_topo_f1_jn_deep_mg = [0.3346659696, 0.5246862943, 0.596730581, 0.6270192217]


def draw_gt_mtl_recall_bj():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.3, 0.55)
    plt.plot(gt_mtl_lambda, gt_mtl_recall_bj, marker='s', color='C0')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$\lambda$", fontsize=20)
    plt.ylabel("Recall", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/gt_mtl_recall_bj.pdf")
    plt.close()


def draw_gt_mtl_recall_jn():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.2, 0.31)
    plt.plot(gt_mtl_lambda, gt_mtl_recall_jn, marker='s', color='C1')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$\lambda$", fontsize=20)
    plt.ylabel("Recall", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/gt_mtl_recall_jn.pdf")
    plt.close()


def draw_gt_mtl_precision_bj():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.2, 0.3)
    plt.plot(gt_mtl_lambda, gt_mtl_precision_bj, marker='s', color='C0')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$\lambda$", fontsize=20)
    plt.ylabel("Precision", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/gt_mtl_precision_bj.pdf")
    plt.close()


def draw_gt_mtl_precision_jn():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.1, 0.2)
    plt.plot(gt_mtl_lambda, gt_mtl_precision_jn, marker='s', color='C1')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$\lambda$", fontsize=20)
    plt.ylabel("Precision", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/gt_mtl_precision_jn.pdf")
    plt.close()


def draw_gt_mtl_f1_bj():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.3, 0.4)
    plt.plot(gt_mtl_lambda, gt_mtl_f1_bj, marker='s', color='#3C76B6')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$\lambda$", fontsize=20)
    plt.ylabel("F1", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/gt_mtl_f1_bj.pdf")
    plt.close()


def draw_gt_mtl_f1_jn():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.2, 0.23)
    plt.plot(gt_mtl_lambda, gt_mtl_f1_jn, marker='s', color='#C14247')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$\lambda$", fontsize=20)
    plt.ylabel("F1", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/gt_mtl_f1_jn.pdf")
    plt.close()


def draw_mr_geo_f1_bj():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.16, 1.1)
    plt.plot(mr_geo_x, mr_geo_f1_bj_edelkamp, marker='s', label='Edelkamp', color="#3C76B6")
    plt.plot(mr_geo_x, mr_geo_f1_bj_cao, marker='^', label='Cao', color="#C14247")
    plt.plot(mr_geo_x, mr_geo_f1_bj_biagioni, marker='d', label='Biagioni', color="#C754B7")
    plt.plot(mr_geo_x, mr_geo_f1_bj_chen, marker='o', label='Chen', color="#6F5B8F")
    plt.plot(mr_geo_x, mr_geo_f1_bj_kharita, marker='<', label='Kharita', color="#F1D11A")
    plt.plot(mr_geo_x, mr_geo_f1_bj_deep_mg_nt, marker='D', label='DeepMG-nt', color="#DC7633")
    plt.plot(mr_geo_x, mr_geo_f1_bj_deep_mg, marker='>', label='DeepMG', color="#8CB551")
    plt.legend(ncol=2)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.xlabel("mt (m)", fontsize=20)
    plt.xlabel("S Res. (m)", fontsize=20)
    plt.ylabel("F1", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/mr_geo_f1_bj.pdf")
    plt.close()


def draw_mr_geo_f1_jn():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.16, 1.0)
    plt.plot(mr_geo_x, mr_geo_f1_jn_edelkamp, marker='s', label='Edelkamp', color="#3C76B6")
    plt.plot(mr_geo_x, mr_geo_f1_jn_cao, marker='^', label='Cao', color="#C14247")
    plt.plot(mr_geo_x, mr_geo_f1_jn_biagioni, marker='d', label='Biagioni', color="#C754B7")
    plt.plot(mr_geo_x, mr_geo_f1_jn_chen, marker='o', label='Chen', color="#6F5B8F")
    plt.plot(mr_geo_x, mr_geo_f1_jn_kharita, marker='<', label='Kharita', color="#F1D11A")
    plt.plot(mr_geo_x, mr_geo_f1_jn_deep_mg_nt, marker='D', label='DeepMG-nt', color="#DC7633")
    plt.plot(mr_geo_x, mr_geo_f1_jn_deep_mg, marker='>', label='DeepMG', color="#8CB551")
    plt.legend(ncol=2)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.xlabel("mt (m)", fontsize=20)
    plt.xlabel("S Res. (m)", fontsize=20)
    plt.ylabel("F1", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/mr_geo_f1_jn.pdf")
    plt.close()


def draw_mr_topo_f1_bj():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.1, 1.1)
    plt.plot(mr_topo_x, mr_topo_f1_bj_edelkamp, marker='s', label='Edelkamp', color="#3C76B6")
    plt.plot(mr_topo_x, mr_topo_f1_bj_cao, marker='^', label='Cao', color="#C14247")
    plt.plot(mr_topo_x, mr_topo_f1_bj_biagioni, marker='d', label='Biagioni', color="#C754B7")
    plt.plot(mr_topo_x, mr_topo_f1_bj_chen, marker='o', label='Chen', color="#6F5B8F")
    plt.plot(mr_topo_x, mr_topo_f1_bj_kharita, marker='<', label='Kharita', color="#F1D11A")
    plt.plot(mr_topo_x, mr_topo_f1_bj_deep_mg_nt, marker='D', label='DeepMG-nt', color="#DC7633")
    plt.plot(mr_topo_x, mr_topo_f1_bj_deep_mg, marker='>', label='DeepMG', color="#8CB551")
    plt.legend(ncol=2)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.xlabel("mt (m)", fontsize=20)
    plt.xlabel("S Res. (m)", fontsize=20)
    plt.ylabel("F1", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/mr_topo_f1_bj.pdf")
    plt.close()


def draw_mr_topo_f1_jn():
    plt.figure(figsize=(4, 4))
    plt.ylim(0.1, 1.0)
    plt.plot(mr_topo_x, mr_topo_f1_jn_edelkamp, marker='s', label='Edelkamp', color="#3C76B6")
    plt.plot(mr_topo_x, mr_topo_f1_jn_cao, marker='^', label='Cao', color="#C14247")
    plt.plot(mr_topo_x, mr_topo_f1_jn_biagioni, marker='d', label='Biagioni', color="#C754B7")
    plt.plot(mr_topo_x, mr_topo_f1_jn_chen, marker='o', label='Chen', color="#6F5B8F")
    plt.plot(mr_topo_x, mr_topo_f1_jn_kharita, marker='<', label='Kharita', color="#F1D11A")
    plt.plot(mr_topo_x, mr_topo_f1_jn_deep_mg_nt, marker='D', label='DeepMG-nt', color="#DC7633")
    plt.plot(mr_topo_x, mr_topo_f1_jn_deep_mg, marker='>', label='DeepMG', color="#8CB551")
    plt.legend(ncol=2)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.xlabel("mt (m)", fontsize=20)
    plt.xlabel("S Res. (m)", fontsize=20)
    plt.ylabel("F1", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/sijie-aaai-2020/mr_topo_f1_jn.pdf")
    plt.close()


if __name__ == '__main__':
    draw_gt_mtl_f1_bj()
    draw_gt_mtl_f1_jn()

    draw_mr_geo_f1_bj()
    draw_mr_geo_f1_jn()

    draw_mr_topo_f1_bj()
    draw_mr_topo_f1_jn()
    print("ok")
