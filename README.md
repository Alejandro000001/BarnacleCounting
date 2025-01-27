My intial approach was to use a CRSNet model as research shows they are the most commonly used for crowd counting and I though this would apply well to barnacle counting. However, a model of that scale proved not only difficult to implement but also difficult to train based on only two images. 

Thus, I moved on to a U-Net model, which is well suited for segmentation and density map generation. This model's architecture allowed for a simpler and more flexible implementation, while still maintaining the highest performance one can realistically achieve with a dataset so small. 

Before that, however, I first had to prepare the images. Some of the images had to be cropped inside the green box. Initially, I created a function that used color detection to locate the green boundary, which then used edge detection and contour analysis. The problem with this approach was not only that the green box was not a color that contrasted a lot against the barnacles, which proved a little hard to detect without building a model to do so (which I couldn't do with just a couple of training images). Another problem was that the green bounding box or frames had multiple smaller ones, which confused the function as to where to crop. And so, I opted for my function to detect the bright yellow ruler instead, which proved to be a solution that worked better. I simply figured out its dimensions and was able to create a bounding box from it. This solution, although it doesn't focus directly on the green box, actually proved to be way more accurate. 

I have included the results from the two testing images: predicted_density_map_unseen1 and 2, which are density maps of the UNet model with an attached prediction count. As you can see, the count is fairly accurate, but it changes with each iteration. Nevertheless, it is a simple and working solution to a problem that lacks enough data. 

That being said, I learned a lot with this task. I did a lot of reasearch not only regarding which model or approach to use at first, but also about the intricacies of the U-Net model itself. I learned about its unique architecture, which includes its contracting and expanding paths, allowing it to capture both low and high-level features. I also learned about how skip connections help preserve spatial information. Overall, this was a great experience. 

If I had more time and, more importantly, more data, I would go back to a CRSNet model as it would be more accurate. 

In order to run the code, you can simply run the jupyter notebook, but you need the necessary images. 
