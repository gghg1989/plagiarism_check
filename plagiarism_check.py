import mosspy
import click
import os
from os import path

def check_plagiarism(file_name, s, d, k):
    limit = 0

    if k == None:
        print('UserID for MOSS is INVALID! Task is aborted.')
        exit()
    else:
        userid = k

    submissions_path = s

    m = mosspy.Moss(userid, "python")
    m.options['n'] = 900

    m.addBaseFile(submissions_path+file_name)

    students_dir = os.listdir(submissions_path)
    for sd in students_dir:
        # if limit >= 10:
        #     break
        if path.exists(submissions_path+sd+'/'+file_name):
            print('uploading...' + sd)
            m.addFile(submissions_path+sd+'/'+file_name)
            limit += 1
    print(str(limit)+' files uploaded.')
    print("Waiting plagiarism checking results from MOSS server...")
    url = m.send() # Submission Report URL

    print ("Report Url: " + url)

    # Save report file
    if d != None:
        print('Start downloading plagiarism check reports...')
        output_path = d
        if not os.path.isdir(output_path):
            os.mkdir(output_path)
        
        m.saveWebPage(url, output_path + "report.html")
        # Download whole report locally including code diff links
        mosspy.download_report(url, output_path, connections=8)
        print('Report is downloaded to ' + output_path + '.')

@click.command()
@click.option('--src', '-s', 's', help='Source directory of submissions. Need to end with /', default='submissions/', type=click.Path(exists=True))
@click.option('--name', '-n', 'n', help='The name of file to check.', type=click.STRING)
@click.option('--save', '-d', 'd', help='Target directory for saving reports.', type=click.Path())
@click.option('--key', '-k', 'k', help='User Key for MOSS system.', default=None, type=click.STRING)

def main(n, s, d, k):
    print('Start checking plagiarism for ' + n + '...')
    check_plagiarism(n, s, d, k)

if __name__ == "__main__":
    main()