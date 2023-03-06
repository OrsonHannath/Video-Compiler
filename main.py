import os
from moviepy.editor import *
from natsort import natsorted

imagesDirectory = r"C:\Users\User\Desktop\Portfolio\ParticleSimulator\cmake-build-debug\SimulatorRenders\Fountain500_Medium\\"
targetFrameRate = 60
deleteAfter = True  # Should the images be deleted after rendering


def compile_video_from_frames(imgs_path, framerate):

    imageClipPaths = []

    directory = natsorted(os.listdir(imgs_path))
    print(directory)

    for filename in directory:
        if filename.endswith(".png"):

            print("Appending Image - " + filename)

            filepath = imgs_path + filename
            imageClipPaths.append(filepath)
            # imageClips.append(ImageClip(filepath).set_duration(1/framerate))

    videoClip = ImageSequenceClip(imageClipPaths, fps=60)

    print("Rendering Clips to Video")
    finalSavePath = imgs_path + "_" + os.path.basename(os.path.dirname(imgs_path)) + "_render.mp4"
    videoClip.write_videofile(finalSavePath, fps=framerate, codec="libx264", threads=6,
                                ffmpeg_params=["-crf", "16"], preset="veryslow")

    # If wanting to delete image files after rendering do so now
    if deleteAfter:
        for filename in directory:
            if filename.endswith(".png"):

                print("Deleting Image - " + filename)
                filepath = imgs_path + filename
                os.remove(filepath)


if __name__ == '__main__':
    compile_video_from_frames(imagesDirectory, targetFrameRate)
