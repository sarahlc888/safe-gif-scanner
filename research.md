## Takeaways from research papers on photosensitivity of epileptic patients.

* Flashing lights between the **frequencies** of 5 to 30 flashes per second (Hertz) are most likely to trigger seizures.
* The **contrast** between alternating dark and bright images shouldn't be greater than 20 candelas per square meter (a technical measure for brightness).
* The **area** that the light stimulus occupies in the field determines how much of the brain gets stimulated. In the case of television viewing at a distance of about nine feet, the area of the flashing stimulus on the screen shouldn't be greater than 25 percent of the total area.
* Static or moving **patterns** of discernable light and dark stripes have the same effect as flashing lights because of the alternation of dark and bright areas. The danger depends on how many and how contrasted the stripes are in the visual field. No more than five pairs of stripes if they are moving within the field of vision and no more than eight pairs if they are static shold be on the screen.  
* Certain **colors** are critical; in particular, the so-called saturated “deep” red. Within the visual spectrum, this color is the one with the longest wavelength and it can be easily eliminated by wearing appropriate optical filters (blue lenses). 

Because there's two main issues here(saturated red transitions and flashes) I'll create two algorithms. The saturated red transition will use [relative luminance](https://www.w3.org/WAI/GL/wiki/Relative_luminance) to measure transitions. The luminance flash algorithm will detect the difference from the previous frame, as done in [this paper](https://www.semanticscholar.org/paper/Automatic-detection-of-flashing-video-content-Carreira-Rodrigues/341e2139f4239882e12d8ee01f4d56532b4cd8ea#paper-header).

How can I actually test this? There's no database of obviously unsafe GIFs for ethics reasons, so I might have to corrupt videos myself. I'll create an algorithm to corrupt videos by adding flashing or deep red to some of the frames randomly. Since the risk of seizure is not binary, but probabilistic, I'll partially use random chance. 

References:

1. [Guide to Accessible Web Design & Development](https://www.section508.gov/content/guide-accessible-web-design-development#flashing)
2. [Shedding Light on Photosensitivity, One of Epilepsy's Most Complex Conditions](https://www.epilepsy.com/article/2014/3/shedding-light-photosensitivity-one-epilepsys-most-complex-conditions-0)


