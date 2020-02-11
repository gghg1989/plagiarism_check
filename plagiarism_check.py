import mosspy

import click

def check_plagiarism(file_name):
    counter = 0      

    limit = 0

    userid = 1

    submissions_path = 'submissions/hw5/'

    m = mosspy.Moss(userid, "python")
    m.options['n'] = 900

    m.addBaseFile(submissions_path+file_name)

    students_dir = os.listdir(submissions_path)
    for d in students_dir:
        # if limit >= 10:
        #     break
        # print('uploading...' + d+'/'+file_name)
        if path.exists(submissions_path+d+'/hw5/'+file_name):
            print('uploading...' + d)
            m.addFile(submissions_path+d+'/hw5/'+file_name)
            limit += 1
    print(str(limit)+' files uploaded.')
    print("Waiting plagiarism checking results from MOSS server...")
    url = m.send() # Submission Report URL

    print ("Report Url: " + url)

    # Save report file
    output_path = 'output/hw5/'
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    m.saveWebPage(url, output_path + "report.html")

    # Download whole report locally including code diff links
    mosspy.download_report(url, output_path, connections=8)

@click.command()
@click.option('-s', '--src', '--source', help='Source directory of submissions', type=click.Path(exists=True))
def main(source):
    print('test' + str(source))

if __name__ == "__main__":
    main()