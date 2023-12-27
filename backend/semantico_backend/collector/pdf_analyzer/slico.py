import skimage.io
from skimage.color import rgb2gray
from skimage.segmentation import slic, chan_vese
from skimage.transform import downscale_local_mean, resize
import matplotlib.pyplot as plt
from skimage.color import label2rgb
from skimage.filters import threshold_otsu
from pdf2image import convert_from_path
import tempfile
import os


def export_pngs(work_path, pdf_path=None):
    if len(os.listdir(work_path)) == 0 and pdf_path:
        images_from_path = convert_from_path(pdf_path, output_folder=work_path,
                                             fmt='png')
    # Sample Image of scikit-image package
    print(f"{sorted(os.listdir(work_path))}")
    png_pages = [skimage.io.imread(os.path.join(work_path, png_path)) for png_path in sorted(os.listdir(work_path))
                 if os.path.splitext(png_path)[1] == '.png']
    return png_pages


def export_segments(png_pages):

    for png_page in png_pages:
        plt.figure(figsize=(16, 24))
        # Applying Simple Linear Iterative
        # Clustering on the image
        # - 50 segments & compactness = 10
        gray_png_page = rgb2gray(png_page)
        shape = gray_png_page.shape
        scaled_png_page = resize(downscale_local_mean(gray_png_page, factors=(8, 8)), shape)

        bin_png_page = (scaled_png_page > .996).astype(int)
        page_segments = chan_vese(bin_png_page, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                                  max_num_iter=12, dt=0.5, init_level_set="checkerboard",
                                  extended_output=False)
        page_slics = slic(bin_png_page, compactness=1,
                          n_segments=96, spacing=[1, 1],
                          enforce_connectivity=True, channel_axis=None,
                          sigma=0, mask=page_segments)

        plt.subplot(3, 2, 1)
        # Plotting the original image
        plt.imshow(gray_png_page, cmap='gray', )

        plt.subplot(3, 2, 2)
        # Plotting the rescaled image
        plt.imshow(scaled_png_page, cmap='gray', vmin=0, vmax=1)

        plt.subplot(3, 2, 3)
        # Plotting bin image
        plt.imshow(bin_png_page, cmap='gray', vmin=0, vmax=1)

        plt.subplot(3, 2, 4)
        # Converts a label image into gray
        plt.imshow(label2rgb(page_segments, png_page, kind='overlay'))

        plt.subplot(3, 2, 5)
        # converts slics to image
        plt.imshow(label2rgb(page_slics, png_page, kind='overlay'))

        plt.show()


def make_work_folder(path):
    path_folder = os.path.splitext(path)[0]
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)
    return path_folder
