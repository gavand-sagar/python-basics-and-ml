using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;

class Program
{
    static void Main()
    {
        using (var session = new InferenceSession("C:\\Users\\Sagar\\Desktop\\ml-quest\\python-basics-and-ml\\session9\\model.onnx"))
        {

            var inputData = new float[]
            {
            1,1
            };

            var tensor = new DenseTensor<float>(inputData, new int[] { 1, 2 });

            var inputs = new List<NamedOnnxValue>
                {
                    NamedOnnxValue.CreateFromTensor("input", tensor)
                };

            using var results = session.Run(inputs);

            var output = results.First().AsEnumerable<float>().ToArray();

            Console.WriteLine("ONNX Predictions (C#):");

            foreach (var val in output)
            {
                // Apply sigmoid
                var sigmoid = 1.0 / (1.0 + Math.Exp(-val));
                Console.WriteLine(sigmoid);
            }
        }

    }
}