import extract, transform, load

if __name__ == '__main__':
    extract.main()
    df = transform.main()
    load.main(df)