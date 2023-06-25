# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

from mindspore import context
from utils.args import get_eval_argparser
from models.train_and_eval import EvalWrapper

def main():
    argparser = get_eval_argparser()
    args = argparser.parse_args()
    context.set_context(mode=context.GRAPH_MODE, device_target=args.device)
    eval_net = EvalWrapper(args.hparams_path, args.ckpt_path)
    eval_net.run_eval()

if __name__ == '__main__':
    main()
