with open(
    r'les11_csv_files_work\theory\sample_640×426.bmp', 'rb'
) as inp_file:
    header = inp_file.read(54)
    res = [255 - val for val in inp_file.read()]
    with open(
        r'les11_csv_files_work\theory\sample_negative.bmp', 'wb'
    ) as out_file:
        out_file.write(header)
        out_file.write(bytes(res))


# with open(r'les11_csv_files_work\theory\sample_640×426.bmp', mode='rb') as in_file:
#     header = in_file.read(54)
#     res = [255 - val for val in in_file.read()]
#     with open(r'les11_csv_files_work\theory\sample_negative.bmp', mode="wb") as out_file:
#         out_file.write(header)
#         out_file.write(bytes(res))
