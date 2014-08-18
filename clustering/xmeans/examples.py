from samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;

from clustering.xmeans import xmeans;

from support import draw_clusters, read_sample, timedcall;

def template_clustering(start_centers, path, tolerance = 0.25, ccore = False):
    sample = read_sample(path);
    
    (ticks, clusters) = timedcall(xmeans, sample, start_centers, 20, ccore);
    print("Sample: ", path, "\t\tExecution time: ", ticks, "Number of clusters: ", len(clusters), "\n");

    draw_clusters(sample, clusters);
    

def cluster_sample1():
    "Start with wrong number of clusters."
    start_centers = [[3.7, 5.5]];
    template_clustering(start_centers, SIMPLE_SAMPLES.SAMPLE_SIMPLE1);
    
def cluster_sample2():
    "Start with wrong number of clusters."
    start_centers = [[3.5, 4.8], [2.6, 2.5]];
    template_clustering(start_centers, SIMPLE_SAMPLES.SAMPLE_SIMPLE2);
    
def cluster_sample3():
    "Start with wrong number of clusters."
    start_centers = [[0.2, 0.1], [4.0, 1.0]];
    template_clustering(start_centers, SIMPLE_SAMPLES.SAMPLE_SIMPLE3);
    
def cluster_sample4():
    start_centers = [[1.5, 0.0], [1.5, 2.0], [1.5, 4.0], [1.5, 6.0], [1.5, 8.0]];
    template_clustering(start_centers, SIMPLE_SAMPLES.SAMPLE_SIMPLE4);
    
def cluster_sample5():
    "Start with wrong number of clusters."
    start_centers = [[0.0, 1.0], [0.0, 0.0]];
    template_clustering(start_centers, SIMPLE_SAMPLES.SAMPLE_SIMPLE5);   
    
def cluster_elongate():
    "Not so applicable for this sample"
    start_centers = [[1.0, 4.5], [3.1, 2.7]];
    template_clustering(start_centers, SIMPLE_SAMPLES.SAMPLE_ELONGATE);

def cluster_lsun():
    "Not so applicable for this sample"
    start_centers = [[1.0, 3.5], [2.0, 0.5], [3.0, 3.0]];
    template_clustering(start_centers, FCPS_SAMPLES.SAMPLE_LSUN);  
    
def cluster_target():
    "Not so applicable for this sample"
    start_centers = [[0.2, 0.2], [0.0, -2.0], [3.0, -3.0], [3.0, 3.0], [-3.0, 3.0], [-3.0, -3.0]];
    template_clustering(start_centers, FCPS_SAMPLES.SAMPLE_TARGET);     

def cluster_two_diamonds():
    "Start with wrong number of clusters."
    start_centers = [[0.8, 0.2]];
    template_clustering(start_centers, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS);
    
def cluster_wing_nut():
    start_centers = [[-1.5, 1.5], [1.5, 1.5]];
    template_clustering(start_centers, FCPS_SAMPLES.SAMPLE_WING_NUT); 
    
def cluster_chainlink():
    start_centers = [[1.1, -1.7, 1.1], [-1.4, 2.5, -1.2]];
    template_clustering(start_centers, FCPS_SAMPLES.SAMPLE_CHAINLINK);     
    
def cluster_hepta():
    "Start with wrong number of clusters."
    start_centers = [[0.0, 0.0, 0.0], [3.0, 0.0, 0.0], [-2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, -3.0, 0.0], [0.0, 0.0, 2.5]];
    template_clustering(start_centers, FCPS_SAMPLES.SAMPLE_HEPTA); 
    
def cluster_tetra():
    start_centers = [[1, 0, 0], [0, 1, 0], [0, -1, 0], [-1, 0, 0]];
    template_clustering(start_centers, FCPS_SAMPLES.SAMPLE_TETRA); 
    
def experiment_execution_time(ccore_flag = False):
    template_clustering([[3.7, 5.5]], SIMPLE_SAMPLES.SAMPLE_SIMPLE1, ccore = ccore_flag);
    template_clustering([[3.5, 4.8], [2.6, 2.5]], SIMPLE_SAMPLES.SAMPLE_SIMPLE2, ccore = ccore_flag);
    template_clustering([[0.2, 0.1], [4.0, 1.0]], SIMPLE_SAMPLES.SAMPLE_SIMPLE3, ccore = ccore_flag);
    template_clustering([[1.5, 0.0], [1.5, 2.0], [1.5, 4.0], [1.5, 6.0], [1.5, 8.0]], SIMPLE_SAMPLES.SAMPLE_SIMPLE4, ccore = ccore_flag);
    template_clustering([[0.0, 1.0], [0.0, 0.0]], SIMPLE_SAMPLES.SAMPLE_SIMPLE5, ccore = ccore_flag);
    template_clustering([[1.0, 4.5], [3.1, 2.7]], SIMPLE_SAMPLES.SAMPLE_ELONGATE, ccore = ccore_flag);
    template_clustering([[1.0, 3.5], [2.0, 0.5], [3.0, 3.0]], FCPS_SAMPLES.SAMPLE_LSUN, ccore = ccore_flag);
    template_clustering([[0.2, 0.2], [0.0, -2.0], [3.0, -3.0], [3.0, 3.0], [-3.0, 3.0], [-3.0, -3.0]], FCPS_SAMPLES.SAMPLE_TARGET, ccore = ccore_flag);
    template_clustering([[0.8, 0.2]], FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, ccore = ccore_flag);
    template_clustering([[-1.5, 1.5], [1.5, 1.5]], FCPS_SAMPLES.SAMPLE_WING_NUT, ccore = ccore_flag);
    template_clustering([[1.1, -1.7, 1.1], [-1.4, 2.5, -1.2]], FCPS_SAMPLES.SAMPLE_CHAINLINK, ccore = ccore_flag);
    template_clustering([[0.0, 0.0, 0.0], [3.0, 0.0, 0.0], [-2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, -3.0, 0.0], [0.0, 0.0, 2.5]], FCPS_SAMPLES.SAMPLE_HEPTA, ccore = ccore_flag)
    template_clustering([[1, 0, 0], [0, 1, 0], [0, -1, 0], [-1, 0, 0]], FCPS_SAMPLES.SAMPLE_TETRA, ccore = ccore_flag);
    
cluster_sample1();
cluster_sample2();
cluster_sample3();
cluster_sample4();
cluster_sample5();
cluster_elongate();
cluster_lsun();
cluster_target();
cluster_two_diamonds();
cluster_wing_nut();
cluster_chainlink();
cluster_hepta();
cluster_tetra();
 
experiment_execution_time(False);   # Python code
experiment_execution_time(True);    # C++ code + Python env.