import os
import re


noann_regex = re.compile('"(.+)"[;.]')
name_regex = re.compile('"(.+)":')
tud_regex = re.compile('(\d+),\s+(\d+),\s+(\d+),\s+(\d+)')

def readidl(images_folder, idlfilename):
    """
    Returns a list of tuples. The first element of a tuple is the full path of the image. The second element of the tuple is 0, if there are no people in the image. If there are people in the image, then the second element of the tuple is a list of tuples. Each tuple is of length 4 (Xmin, Ymin, Xmax, Ymax). So, number of elements in the list would be equal to the number of people annotated in the image.
    """
    fid = open(idlfilename, 'r')
    output = []
    for line in fid:
        line = line.strip()
        if re.match(noann_regex, line):
            name = list(map(str, re.findall(noann_regex, line)))[0]
            #fname = os.path.join(images_folder, name)
            output.append((name, 0))
        else:
            #name = list(map(str, re.findall(name_regex, line)))[0]
            name = list(map(str, re.findall(name_regex, line)))[0]
            #fname = os.path.join(images_folder, name)
            annotations = re.findall(tud_regex, line)
            annotations = list(map(lambda x: tuple(map(int, list(x))), annotations))
            #annotations = list(map(lambda x: tuple(map(int, list(x))), annotations))
            output.append((name, annotations))
    return output

def get_data(images_folder, idlfile):
    return readidl(images_folder, idlfile)


if __name__ == "__main__":
    # The following is for positive images in training set
    BAHNHOF = get_data("/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/BAHNHOF", "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/BAHNHOF/bahnhof-annot.idl")

    CROSSING = get_data("/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/CROSSING", "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/CROSSING/crossing-annot.idl")
 
    JELMOLI = get_data("/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/JELMOLI", "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/JELMOLI/jelmoli-annot.idl")

    LINTHESCHER = get_data("/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/LINTHESCHER", "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/LINTHESCHER/linthescher-annot.idl")
    
    LOEWENPLATZ  = get_data("/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/LOEWENPLATZ", "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/LOEWENPLATZ/lp-annot.idl")

    SUNNYDAY = get_data("/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/SUNNY-DAY", "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/SUNNY-DAY/sunny_day-annot.idl")
    
    # save to file
        
    for row in BAHNHOF:
        
        file_name = row[0]

        print(file_name)
        annot_folder = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/BAHNHOF"
        if not os.path.exists(annot_folder):
               os.makedirs(annot_folder)

        fname = os.path.join(annot_folder, os.path.basename(file_name) + str(".txt") )
        f = open(fname, 'w')
        annot = row[1] # list of tuples
        if annot !=0:
            for annotelems in annot: # annotelems is tuple of (Xmin, Ymin, Xmax, Ymax)
                Xmin = annotelems[0]
                Ymin = annotelems[1]
                Xmax = annotelems[2]
                Ymax = annotelems[3]
                f.write(str(Xmin) + " " + str(Ymin) + " " + str(Xmax) + " " + str(Ymax) + '\n' )
            f.close()


    for row in CROSSING:
        
        file_name = row[0]

        print(file_name)
        annot_folder = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/CROSSING"
        if not os.path.exists(annot_folder):
               os.makedirs(annot_folder)

        fname = os.path.join(annot_folder, os.path.basename(file_name) + str(".txt") )
        f = open(fname, 'w')
        annot = row[1] # list of tuples
        if annot !=0:
            for annotelems in annot: # annotelems is tuple of (Xmin, Ymin, Xmax, Ymax)
                Xmin = annotelems[0]
                Ymin = annotelems[1]
                Xmax = annotelems[2]
                Ymax = annotelems[3]
                f.write(str(Xmin) + " " + str(Ymin) + " " + str(Xmax) + " " + str(Ymax) + '\n' )
            f.close()

    
    for row in JELMOLI:

        file_name = row[0]

        print(file_name)
        annot_folder = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/JELMOLI"
        if not os.path.exists(annot_folder):
               os.makedirs(annot_folder)

        fname = os.path.join(annot_folder, os.path.basename(file_name) + str(".txt") )
        f = open(fname, 'w')
        annot = row[1] # list of tuples
        if annot !=0:
            for annotelems in annot: # annotelems is tuple of (Xmin, Ymin, Xmax, Ymax)
                Xmin = annotelems[0]
                Ymin = annotelems[1]
                Xmax = annotelems[2]
                Ymax = annotelems[3]
                f.write(str(Xmin) + " " + str(Ymin) + " " + str(Xmax) + " " + str(Ymax) + '\n' )
            f.close()


    for row in LINTHESCHER:

        file_name = row[0]

        print(file_name)
        annot_folder = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/LINTHESCHER"
        if not os.path.exists(annot_folder):
               os.makedirs(annot_folder)

        fname = os.path.join(annot_folder, os.path.basename(file_name) + str(".txt") )
        f = open(fname, 'w')
        annot = row[1] # list of tuples
        if annot !=0:
            for annotelems in annot: # annotelems is tuple of (Xmin, Ymin, Xmax, Ymax)
                Xmin = annotelems[0]
                Ymin = annotelems[1]
                Xmax = annotelems[2]
                Ymax = annotelems[3]
                f.write(str(Xmin) + " " + str(Ymin) + " " + str(Xmax) + " " + str(Ymax) + '\n' )
            f.close()

    for row in LOEWENPLATZ:

        file_name = row[0]

        print(file_name)
        annot_folder = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/LOEWENPLATZ"
        if not os.path.exists(annot_folder):
               os.makedirs(annot_folder)

        fname = os.path.join(annot_folder, os.path.basename(file_name) + str(".txt") )
        f = open(fname, 'w')
        annot = row[1] # list of tuples
        if annot !=0:
            for annotelems in annot: # annotelems is tuple of (Xmin, Ymin, Xmax, Ymax)
                Xmin = annotelems[0]
                Ymin = annotelems[1]
                Xmax = annotelems[2]
                Ymax = annotelems[3]
                f.write(str(Xmin) + " " + str(Ymin) + " " + str(Xmax) + " " + str(Ymax) + '\n' )
            f.close()

    for row in SUNNYDAY:

        file_name = row[0]

        print(file_name)
        annot_folder = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/SUNNY-DAY"
        if not os.path.exists(annot_folder):
               os.makedirs(annot_folder)

        fname = os.path.join(annot_folder, os.path.basename(file_name) + str(".txt") )
        f = open(fname, 'w')
        annot = row[1] # list of tuples
        if annot !=0:
            for annotelems in annot: # annotelems is tuple of (Xmin, Ymin, Xmax, Ymax)
                Xmin = annotelems[0]
                Ymin = annotelems[1]
                Xmax = annotelems[2]
                Ymax = annotelems[3]
                f.write(str(Xmin) + " " + str(Ymin) + " " + str(Xmax) + " " + str(Ymax) + '\n' )
            f.close()

